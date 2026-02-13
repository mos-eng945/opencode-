from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from pydantic import Field
import uvicorn
app = FastAPI() 
class User(BaseModel):
    name: str = Field(default="alex", min_length=2, max_length=10)
    age: int    = Field(default=18, gt=0, le=100)
@app.post("/user/")
def read_user(user:User):
    return user

class Item(BaseModel):
    name: str
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float = 0.00
@app.post("/items/")
def create_item(item: Item):
            return item

class User2(BaseModel):
    name: str
    email: str  # 修正字段名为 email

    @field_validator("email")  # 修正拼写错误
    def validate_email(cls, value):
        # 自定义校验逻辑
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value@app.post("/user2/")
def user1(user: User2):
    return User2
if __name__ == "__main__":
    uvicorn.run("main07:app", host="127.0.0.1", port=8000, reload=True)