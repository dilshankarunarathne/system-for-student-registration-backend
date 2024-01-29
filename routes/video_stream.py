from fastapi import APIRouter

router = APIRouter(
    prefix="/api/video-stream",
    tags=["video-stream"],
    responses={404: {"description": "The requested url was not found"}},
)

@app.websocket("/ws/video")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        # Handle the video stream data here
        