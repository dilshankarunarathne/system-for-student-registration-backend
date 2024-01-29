import base64
import re

import cv2
import numpy as np
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket

from face_rec.detector import recognize_faces_in_base64
from routes import auth_route, attendance_route, student_route, course_route, lecturer_route, class_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_route.router)
app.include_router(attendance_route.router)
app.include_router(student_route.router)
app.include_router(course_route.router)
app.include_router(lecturer_route.router)
app.include_router(class_route.router)


@app.websocket_route("/ws/register")
async def websocket_endpoint(
        websocket: WebSocket,
        student_id: str,
):
    count = 0
    try:
        await websocket.accept()
        while count < 30:
            count += 1
            data = await websocket.receive_text()

            base64_str = re.search(r'base64,(.*)', data).group(1)
            frame_data = base64.b64decode(base64_str)
            nparr = np.frombuffer(frame_data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if frame is None:
                print("error frame is none")
            else:
                print("Image decoded successfully")
            print(frame)

            save_image(frame, class_name)
            store_image_model_info(class_name, student_id)

    except Exception as e:
        print(f"Error: {e}")


@app.websocket_route("/ws/video")
async def websocket_endpoint(
        websocket: WebSocket
):
    try:
        await websocket.accept()
        while True:
            data = await websocket.receive_text()

            base64_str = re.search(r'base64,(.*)', data).group(1)
            frame_data = base64.b64decode(base64_str)
            nparr = np.frombuffer(frame_data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if frame is None:
                print("error frame is none")
            else:
                print("Image decoded successfully")
            print(frame)
            faces = recognize_faces_in_base64(frame)

            await websocket.send_text(faces)
    except Exception as e:
        print(f"Error: {e}")
