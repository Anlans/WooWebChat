from typing import Dict, Optional
from schemas.base import User


class RoomConnectionManager:

    def __init__(self):
        self._users_socket: Dict[str, User]

    def user_add_login_room(self, user: User):
        if user.phone_number not in self._users_socket:
            self._users_socket[user.phone_number] = user

