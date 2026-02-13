#Form表单参数验证,anootated
from fastapi import FastAPI, Form
from pydantic import BaseModel, Field
import uvicorn
from typing import Annotated
app = FastAPI()

@app.post("/login1/")
def login1(username: str, password: str=Form(default="123456", min_length=6, max_length=12)):

    return {"msg": "login1 success","username": username, "password": password}

class user1(BaseModel):
    username: str=Field(min_length=2, max_length=10)
    password: str
@app.post("/user2/")
def user2(user1: Annotated[user1, Form()]):
    return user1

if __name__ == "__main__":
    uvicorn.run("main08:app", host="127.0.0.1", port=8000, reload=True)