# JSON请求体post
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()
class User(BaseModel):
    name: str="张三"
    age: int=0
    password: str
    id: int
@app.post("/users")
def create_user(user: dict):
    return user
@app.post("/users2")
def create_user2(user: User):
    return user
if __name__ == "__main__":

    uvicorn.run("main03:app", host="0.0.0.0", port=8000,reload=True)