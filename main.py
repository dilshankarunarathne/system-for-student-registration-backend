from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes import auth_route, attendance_route

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
