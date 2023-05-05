from app.db.todos import (
    get_todos,
    create_todo,
    get_todo_by_id as db_get_todo_by_id,
    update_todo,
    delete_todo,
)

from app.db.models import TodoCreate, TodoUpdate
from sqlalchemy.orm import Session


def get_all_todos(db: Session):
    return get_todos(db)


def create_new_todo(db: Session, todo: TodoCreate):
    create_todo(db, todo.task)


def get_todo_by_id(db: Session, todo_id: int):
    return db_get_todo_by_id(db, todo_id)


def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    update_todo(
        db,
        todo_id,
        task=todo.task,
        completed=todo.completed,
    )


def delete_todo_by_id(db: Session, todo_id: int):
    delete_todo(db, todo_id)