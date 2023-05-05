from fastapi import FastAPI
from app.routes.router import router as todo_router

app = FastAPI()

app.include_router(todo_router, prefix="/todos", tags=["todos"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)