from websocket import WebSocket

from face_rec.detector import recognize_faces_in_base64
from main import app


@app.websocket("/ws/video")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        faces = recognize_faces_in_base64(data)
