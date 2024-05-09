from fastapi import FastAPI, APIRouter, WebSocket, status
from starlette.endpoints import WebSocketEndpoint
from faker import Faker
from typing import Optional, Any
from schemas.base import User


router_char = APIRouter(tags=["聊天室"])


@router_char.websocket_route("/api/v1/room/socketws/")
class ChatRoomWebSocket(WebSocketEndpoint):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 每个当前会话都会执行一次下面的东西，初始化
        self.curr_user: Optional[User] = None

    # 客户端连接
    async def on_connect(self, _websocket: WebSocket) -> None:
        pass

    # 客户端断开
    async def on_disconnect(self, _websocket: WebSocket, _close_code: int) -> None:
        pass

    # 接收客户端发送消息
    async def on_receive(self, _websocket: WebSocket, msg: Any) -> None:
        pass
