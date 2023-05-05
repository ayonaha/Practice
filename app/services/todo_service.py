
import app.db.models
from app.db import todos

def get_all_todos(db):
    return todos.get_todos(db)


def create_new_todo(db, task):
    todos.create_todo(db, task)


def get_todo_by_id(db, todo_id: int):
    todo = todos.get_todo_by_id(db, todo_id)
    return todo


def update_todo(db, todo_id, task, completed):
    return todos.update_todo(db, todo_id, task, completed)

def delete_todo_by_id(db, todo_id):
    return todos.delete_todo(db, todo_id)