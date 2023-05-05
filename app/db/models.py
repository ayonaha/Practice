from typing import Optional

from pydantic import BaseModel


class Todo(BaseModel):
    task: str
#
#
# class TodoCreate(Todo):
#     pass
#
#
# class TodoUpdate(Todo):
#     completed: Optional[bool] = False
#
#     class Config:
#         orm_mode = True