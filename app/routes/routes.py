from fastapi.templating import Jinja2Templates
from app.services.todo_service import TodoService
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter()
todo_service = TodoService()

@router.get("/")
async def home(request: Request):
    todos = todo_service.get_all_todos()
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@router.post("/add")
async def add(request: Request, task: str = Form(...)):
    todo_service.create_new_todo(TodoCreate(task=task))
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/edit/{todo_id}")
async def edit(request: Request, todo_id: int):
    todo = todo_service.get_todo_by_id(todo_id)
    return templates.TemplateResponse("edit.html", {"request": request, "todo": todo})

@router.post("/edit/{todo_id}")
async def update(request: Request, todo_id: int, task: str = Form(...), completed: bool = Form(False)):
    todo_service.update_todo(todo_id, TodoUpdate(task=task, completed=completed))
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/delete/{todo_id}")
async def delete(request: Request, todo_id: int):
    todo_service.delete_todo_by_id(todo_id)
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)