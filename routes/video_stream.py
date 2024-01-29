from starlette.websockets import WebSocket
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

from face_rec.detector import recognize_faces_in_base64
from main import app


async def websocket_endpoint(
        websocket: WebSocket
):
    try:
        print("websocket_endpoint")
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            faces = recognize_faces_in_base64(data)
            await websocket.send_text(faces)
    except Exception as e:
        print(f"Error: {e}")
