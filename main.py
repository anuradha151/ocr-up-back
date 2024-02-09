from fastapi import FastAPI,File, UploadFile;
from fastapi.middleware.cors import CORSMiddleware;
from ml_txt_detection import detect

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():    
    return {"Hellow": "World"}

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile=File(...)):
    reponse = detect(file.file)    
    return {
        "text":reponse
    }