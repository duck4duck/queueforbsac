from datetime import datetime

from pydantic import BaseModel

from app.core.models.base import Suggestion


## ЭТО ВСЕ МОИ ДЕЙСТВИЯ КАСАТЕЛЬНО ЮЗЕРА
class User(BaseModel):
    name: str
    photo_url: str | None = None
    tg_id: str


class UserCreate(BaseModel):
    pass


class UserUpdate(User):
    pass


class DeleteUserFromEvent(User):
    event_id: int


class AddUserInEvent(User):
    event_id: int


#####################################


# ЭТО ВСЁ КАСАТЕЛЬНО САМИХ ПРЕДМЕТОВ
class SubjectCreate(BaseModel):
    subject: str


class SubjectDelete(SubjectCreate):
    pass


############################


# ЭТО ВСЁ ПРО ИВЕНТЫ(ВОЗМОЖНЫ ДОРАБОТКИ)
class Event(BaseModel):
    name: str
    date: datetime
    subject: str


class EventCreate(Event):
    pass


class EventDelete(Event):
    pass


##################################
class Suggestion(BaseModel):
    text: str
    state: str
    from_user: int
    to_user: int
    tg_id: str
    event_id: int
