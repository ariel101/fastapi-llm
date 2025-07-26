import os
from dotenv import load_dotenv
import torch
from diffusers import StableDiffusionPipeline

# Cargar variables de entorno desde .env
load_dotenv()
MODEL_PATH = os.getenv("SD_MODEL_PATH")

pipe = StableDiffusionPipeline.from_single_file(
    MODEL_PATH,
    torch_dtype=torch.float16,
    safety_checker=None
).to("cuda")

def generate_image(prompt: str, output_path: str) -> str:
    image = pipe(prompt).images[0]
    image.save(output_path)
    return output_path
