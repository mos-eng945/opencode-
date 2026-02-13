#设置查询参数
from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/query1")
def page_limit(page: int, limit: int):
    return {"message": f"page {page} limit {limit}"}
@app.get("/query2")
def page_limit2(page: int , limit= None ):
    if limit is None:
        limit = 10
    else:
        return {"message": f"page {page} limit {limit}"}

if __name__ == "__main__":

    uvicorn.run("main02:app", host="0.0.0.0", port=8000,reload=True)