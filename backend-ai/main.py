from fastapi import  FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from core import deteccion
import shutil
import uvicorn
app = FastAPI()

#enable_cors()
origins = [
    "http://localhost:8080",
    ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/img")
async def upload_img(file: UploadFile = File(...)):
    with open(f'upload/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # aca deberia de ir la funcion para poder detectar la imagen
    detect = deteccion(file)
    return {'message': f'Imagen {file.filename} analizada!', 'detect': detect}

if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=4000, reload=True)

