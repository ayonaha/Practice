from fastapi import APIRouter, Request, Form, status, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from app.services import todo_service
from app.core.config import database
# from app.core.config.database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")


def get_db():
    db = Session(database.engine)
    try:
        yield db
    finally:
        db.close()
print(get_db)
@router.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    todos = todo_service.get_all_todos(db)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})


@router.post("/add")
async def add(request: Request, task: str = Form(...), db: Session = Depends(get_db)):
    todo = todo_service.create_new_todo(db, task)
    return RedirectResponse(url=router.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)


@router.get("/edit/{todo_id}")
async def edit(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = todo_service.get_todo_by_id(db, todo_id)
    return templates.TemplateResponse("edit.html", {"request": request, "todo": todo})


@router.post("/edit/{todo_id}")
async def update(request: Request, todo_id: int, task: str = Form(...), completed: bool = Form(...), db: Session = Depends(get_db)):
    todo = todo_service.update_todo(db, todo_id, task, completed)
    return RedirectResponse(url=router.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)


@router.get("/delete/{todo_id}")
async def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo_service.delete_todo_by_id(db, todo_id)
    return RedirectResponse(url=router.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)