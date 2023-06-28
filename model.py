from pydantic import BaseModel
# 2개의 필드만 허용하는 pydantic 모델을 만든다
class Todo(BaseModel):
    id : int
    item : str
# POST라우트에 사용 POST의 구조를 정의
    class Config: # sample
        schema_extra = {
            'example':{
                "id" : 1,
                "item" : "example schema"
            }
        }

# UPDATE라우트의 요청 바디용 모델 (요청구조)
class TodoItem(BaseModel):
    item : str

    class Config: # sample
        schema_extra = {
            "example":{
            'item':'read the next chapter of the book.'
            }
        }