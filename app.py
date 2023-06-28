from fastapi import FastAPI
from todo import todo_router # APIRouter 객체 import
app = FastAPI()

@app.get('/')
async def welcome():
    return {
        'message':'hello'
    }

app.include_router(todo_router)