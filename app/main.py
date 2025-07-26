from fastapi import FastAPI
from app.models import PromptRequest
from app.generator import generate_image
import os
import uuid

app = FastAPI()

@app.post("/generate")
def generate(data: PromptRequest):
    filename = f"{uuid.uuid4().hex}.png"
    output_path = os.path.join("assets/generated", filename)
    generate_image(data.prompt, output_path)
    return {"filename": filename, "path": output_path}
