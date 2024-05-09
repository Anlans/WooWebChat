from dataclasses import dataclass
from pydantic import BaseModel
from starlette.websockets import WebSocket


@dataclass
class User:
    phone_number: str
    username: str
    websocket: WebSocket
