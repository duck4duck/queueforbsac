import json
from typing import List

from fastapi import APIRouter
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


ws_router = APIRouter()

manager = ConnectionManager()


users: dict[str, List[str]] = {}

all_queues: dict[str, List[str]] = {}


@ws_router.get("/hello")
async def hello():
    return {"hello": "world"}


@ws_router.websocket("/ws/queue")
async def ws_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            data = json.loads(message)
            if data["type"] == "message":
                await websocket.send_text("some data")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("disconnect {websocket}", websocket)
