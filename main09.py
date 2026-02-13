#同步异步
from fastapi import FastAPI
import uvicorn
import  time
import asyncio


app = FastAPI()
@app.get("/sync/")
def sync_endpoint():
    time.sleep(5)  # 模拟耗时操作
    return {"message": "This is a synchronous endpoint"}
@app.get("/async/")
async def async_endpoint():
    await asyncio.sleep(5)  # 模拟耗时操作
    
    return {"message": "This is an asynchronous endpoint"}







if __name__ == "__main__":
    uvicorn.run("main09:app", host="127.0.0.1", port=8000, reload=True)