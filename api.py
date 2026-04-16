import sys
import os
import json
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from typing import List
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.post("/generate")
async def generate(
    topic: str = Form(...),
    file_type: str = Form(...),
    sources: str = Form("[]"),
    pdfs: List[UploadFile] = File(default=[])
):
    url_list = json.loads(sources)
    
    # save uploaded pdfs temporarily
    pdf_paths = []
    for pdf in pdfs:
        path = os.path.join(BASE_DIR, pdf.filename)
        with open(path, "wb") as f:
            shutil.copyfileobj(pdf.file, f)
        pdf_paths.append(path)

    # combine urls and pdf paths into sources list
    all_sources = url_list + pdf_paths

    cmd = [sys.executable, "generate.py", topic, file_type] + all_sources
    subprocess.run(cmd, cwd=BASE_DIR)

    # cleanup uploaded pdfs
    for path in pdf_paths:
        os.remove(path)

    filename = topic.replace(" ", "_") + "." + file_type
    filepath = os.path.join(BASE_DIR, filename)
    return FileResponse(filepath, filename=filename)