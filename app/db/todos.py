
from app.db.models import Todo

from app.db.models import TodoCreate, TodoUpdate
from sqlalchemy.orm import Session


def get_todos(db):
    return db.query(Todo).order_by(Todo.id.desc()).all()


def create_todo(db, task: str):
    todo = Todo(task=task)
    db.add(todo)
    db.commit()


def get_all_todos(db: Session):
    return get_todos(db)


def create_new_todo(db: Session, todo: TodoCreate):
    create_todo(db, todo.task)


def get_todo_by_id(db, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo(db, todo_id: int, task: str, completed: bool):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    todo.task = task
    todo.completed = completed
    db.commit()


def delete_todo(db, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()


