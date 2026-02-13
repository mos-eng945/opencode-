##文件上传

from fastapi import FastAPI ,File,UploadFile
import uvicorn
app = FastAPI()
@app.post("/uploadfile/")
def create_upload_file(file: bytes = File(...)):
    with open("./data/file.jpg", "wb") as f:
        f.write(file)
@app.post("/uploadfile2/")
async def create_upload_file2(file: UploadFile):
    with open(f"./data/{file.filename}", "wb") as f:
        content = await file.read()
        f.write(content)    
               
         
    return {"msg":"upload success"}

@app.post("/batch-uploadfile/")
async def create_batch_upload_file(files: list[UploadFile]):
  
    return { "file_count": len(files), "file_names": [file.filename for file in files]}
if __name__ == "__main__":
    uvicorn.run("main10:app", host="127.0.0.1", port=8000)