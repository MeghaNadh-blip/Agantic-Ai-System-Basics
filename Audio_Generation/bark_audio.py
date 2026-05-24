# Import Libraries
from transformers import AutoProcessor, AutoModel
from IPython.display import Audio

# Load Processor and Model
processor = AutoProcessor.from_pretrained("suno/bark-small")
model = AutoModel.from_pretrained("suno/bark-small")

# Input Text
inputs = processor(
    text="Hello, the girl looks so cute",
    return_tensors="pt",
)

# Generate Speech
speech = model.generate(**inputs, do_sample=True)

# Sampling Rate
sampling_rate = model.generation_config.sample_rate

# Play Audio
Audio(
    speech.cpu().numpy().squeeze(),
    rate=sampling_rate
)
