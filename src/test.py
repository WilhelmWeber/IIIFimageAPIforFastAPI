from iafa import imageapi
from fastapi import FastAPI, Response
import pathlib

app = FastAPI()
ia = imageapi.imageAPI(version=2, pathPrefix='http://localhost:8000/api/v1/image')
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent

@app.get('/api/v1/image/{imageIdentifier}/info.json')
def infoRead(imageIdentifier: str):
    imagepath = PROJECT_ROOT.joinpath('..', 'public', imageIdentifier)
    processed = ia.returnInfo(imagePath=imagepath, identifier=imageIdentifier)
    return processed

@app.get('/api/v1/image/{imageIdentifier}/{req_path:path}')
def imageRead(imageIdentifier: str, req_path: str):
    imagepath = PROJECT_ROOT.joinpath('..', 'public', imageIdentifier)
    processed = ia.returnImage(imagePath=imagepath, reqPath=req_path)
    return processed