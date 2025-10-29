from typing import List

from pydantic import BaseModel


class BaseAction(BaseModel):
    event: str
    id: int
    queue: List[str] | None = None


class AddUserAction(BaseAction):
    type: str = "add"


class RemoveUserAction(BaseAction):
    type: str = "remove"


class SubscribeUserAction(BaseAction):
    type: str = "subscribe"


class UnsubscribeUserAction(BaseAction):
    type: str = "unsubscribe"


class SwapUserAction(BaseAction):
    swap_to_user_id: int
    type: str = "swap"
