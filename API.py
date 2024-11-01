from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import pandas as pd
import numpy as np

app = FastAPI()


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # for ensuring the correct file format
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only .xls files are allowed.")
    
    # Save file locally
    try:
        with open(f"/Users/moiz/Documents/espark_consultant_group/uploads/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "File upload failed", "error": str(e)})

    return JSONResponse(status_code=200, content={"message": "File uploaded successfully"})


