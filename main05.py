#设置查询参数 alias description gt le min_length max_length 
from fastapi import FastAPI, Query
import uvicorn      
app = FastAPI()
@app.get("/items")
def query1(item_id: int = Query(alias="id"), q:str= "123"):
    if q is None:
        return {"item_id": item_id} 
    else:
        return {"item_id": item_id, "q": q}
@app.get("/items2")
def query2(item_id: int = Query(...,min_length=2,max_length=10), q: str = Query("ah")):

    return {"item_id": item_id, "q": q}
@app.get("/items3")
def query3(item_id: int = Query(0,gt=0,le=100,description="你好吖" )):
    return {"item_id": item_id}
if __name__ == "__main__":
    uvicorn.run("main05:app", host="0.0.0.0", port=8000, reload=True)
    
    