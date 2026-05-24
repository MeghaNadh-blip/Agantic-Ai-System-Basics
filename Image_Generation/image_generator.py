# Import Libraries
from transformers import pipeline
import torch
from diffusers import DiffusionPipeline

# Load Stable Diffusion Model
generator = DiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4"
)

# Use GPU
generator.to("cuda")

# Prompt
prompt = "a group of people on the beach"

# Generate Image
image = generator(prompt).images[0]

# Display Image
display(image)
