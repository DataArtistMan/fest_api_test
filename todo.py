from fastapi import FastAPI, APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory='templates/')

# 원래는 if문으로 처리 가능
@todo_router.post("/todo", status_code=201) # 리스트에 todo 추가
async def add_todo(request : Request, todo:Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo) # todo에 Todo클래스 안 id, item을 저장
    return templates.TemplateResponse('todo.html', {
        'request':request,
        'todos':todo_list
    })

@todo_router.get('/todo', response_model=TodoItems) # 조회
async def retrieve_todo(request : Request):
    return templates.TemplateResponse('todo.html', {
        'request':request,
        'todo':'todo_list'
    })

# todo의 ID를 경로 매개변수에 추가
@todo_router.get("/todo/{todo_id}") # {todo_id}가 경로 매개변수
async def get_single_todo(request:Request,todo_id:int = Path(...,title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse({
                'todo.html',{
                    'request':request,
                    'todo':todo
                }
            })
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )
    

@todo_router.put('/todo/{todo_id}') #{json}/1(int)
async def update_todo(todo_data: TodoItem, todo_id : int = Path(...,title = 'The ID of the todo to updated')) -> dict:
    for todo in todo_list:
        if todo.id == todo_id: #todo이름의 dict의 id와 요청한 todo_id가 같으면
            todo.item = todo_data.item # todo dict의 item (key)를 요청한 todo_data의 딕셔너리의 item으로 대입
            return {
                'message' : 'Todo updated successfully'
            }
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        details = "Todo with supplied Id doesn't exist",
    )


@todo_router.delete('/todo/{todo_id}')
async def delete_single_todo(todo_id:int)->dict:
    for i in range(todo_list):
        todo = todo_list[i]
        if todo.id == todo_id: #딕셔너리의 id
            todo_list.pop(i)
            return {
                'message':'Todo deleted successfully'
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Todo with supplied ID does not exist",
    )
    
@todo_router.delete('/todo')
async def delete_all_todo()->dict:
    todo_list.clear()
    return {
        'message':'Todo deleted successfully'
    }

@todo_router.get('/todo', response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        'todos':todo_list
    }