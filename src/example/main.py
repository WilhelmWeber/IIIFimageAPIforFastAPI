from iafa import imageapi
from fastapi import FastAPI, Response

app = FastAPI()
ia: imageapi.imageAPI = imageapi.imageAPI(version=2, pathPrefix='http://localhost:8000/api/v1/image')

@app.get('/api/v1/image/{imageIdentifier}/info.json')
def infoRead(imageIdentifier: str):
    imagepath: str = f"../../public/{imageIdentifier}"
    processed = ia.info(imagePath=imagepath, identifier=imageIdentifier)
    return processed

@app.get('/api/v1/image/{imageIdentifier}/{req_path:path}')
def imageRead(imageIdentifier: str, req_path: str):
    imagepath: str = f"../../public/{imageIdentifier}"
    processed = ia.executor(imagePath=imagepath, reqPath=req_path)
    return Response(processed[0], media_type=processed[1])