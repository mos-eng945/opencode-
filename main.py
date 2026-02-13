#设置路由
from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/args/{id}")
def path_arg_1(id):
    return {"message": f"id {id}"}
@app.get("/args4/{id}/{name}")
def path_arg_2(id: int, name: str):
    return {"message": f"id {id}, name {name}"}
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True)