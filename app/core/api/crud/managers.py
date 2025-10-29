import json
from typing import List, Any

from fastapi import APIRouter
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect

from app.core.api.crud.validation import data_validate


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

all_queues: dict[str, List[Any]] = {}


@ws_router.websocket("/ws/queue")
async def ws_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            raw = json.loads(message)
            data = data_validate(raw)
            if data.type == "add":
                if data.event not in all_queues:
                    all_queues[data.event] = []
                if data.id in all_queues[data.event]:
                    raise Exception(f"Duplicate event '{data.event}'")
                all_queues[data.event].append(data.id)
            print(all_queues)
            new_data = data.model_dump()
            new_data["queue"] = all_queues[data.event]
            await websocket.send_text(json.dumps(new_data))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("disconnect {websocket}", websocket)
