from sqlalchemy.orm import Session
from app.db import models


def get_todos(db: Session):
    return db.query(models.Todo).order_by(models.Todo.id.desc()).all()


def create_todo(db: Session, task: str):
    db_todo = models.Todo(task=task)
    db.add(db_todo)
    db.commit()  # ここでcommitする
    db.refresh(db_todo)
    return db_todo



def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def update_todo(db: Session, todo_id: int, task: str, completed: bool):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db_todo.task = task
    db_todo.completed = completed
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(db_todo)
    db.commit()