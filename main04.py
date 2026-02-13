#union list 路径参数,查询参数,如果有值默认可选
from fastapi import FastAPI
from typing import Optional
from typing import Union,List
import uvicorn
app = FastAPI()
@app.get("/items/{item_id}")
def read_item(item_id: int, q:str= "123"):
    if q is None:
        return {"item_id": item_id} 
    else:
        return {"item_id": item_id, "q": q}
@app.get("/items2/{item_id}")
def read_item2(item_id: int=0, q: Union[str,int]="颤三"):

    return {"item_id": item_id, "q": q}
@app.get("/items3/{item_id}")
def read_items(item_id: int, q:list[int]):
    return {"item_id": item_id, "q": q}
            
if __name__ == "__main__":
    uvicorn.run("main04:app", host="0.0.0.0", port=8000,reload=True)