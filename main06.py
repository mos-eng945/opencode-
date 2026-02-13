#enmu ge path
from fastapi import FastAPI,Path
import uvicorn
from pydantic import BaseModel
app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
@app.get("/items2/{item_id}")
def read_item2(item_id: int = Path(gt=0,lt=100,alias="id")):
    return {"item_id": item_id}
from enum import Enum
class ModerName(str, Enum):
    alexnet = "1"
    resnet = "2"
    lenet = "3"
@app.get("/items3/{model}")
def read_item3(model: ModerName):
    return {"model": model}

if __name__ == "__main__":
    uvicorn.run("main06:app", host="0.0.0.0", port=8000, reload=True)