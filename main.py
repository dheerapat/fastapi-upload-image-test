from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/files/")
async def create_file(img: bytes = File()):
    return {"file_size": len(img)}

@app.post("/uploadfile/")
async def create_upload_file(img: UploadFile):
    file_location = f"files/{img.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(img.file.read())
    return {"info": f"file '{img.filename}' saved at '{file_location}'"}