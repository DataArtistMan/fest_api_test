from fastapi import FastAPI, APIRouter, Path
from model import Todo, TodoItem

todo_router = APIRouter()

todo_list = []
# 원래는 if문으로 처리 가능
@todo_router.post("/todo") # 리스트에 todo 추가
async def add_todo(todo:Todo) -> dict:
    todo_list.append(todo) # todo에 Todo클래스 안 id, item을 저장
    return {
        'message' : 'todo added successfully'
    }

@todo_router.get('/todo') # 조회
async def retrieve_todo():
    return {
        'todo':'todo_list'
    }

# todo의 ID를 경로 매개변수에 추가
@todo_router.get("/todo/{todo_id}") # {todo_id}가 경로 매개변수
async def get_single_todo(todo_id:int = Path(...,title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                'todo':todo
            }
    return {
        'message' : "Todo with supplied ID doesn't exisit"
    }