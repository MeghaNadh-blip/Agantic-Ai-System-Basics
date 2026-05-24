# Import Libraries
from transformers import AutoProcessor, MusicgenForConditionalGeneration
from IPython.display import Audio

# Load Processor and Model
processor = AutoProcessor.from_pretrained(
    "facebook/musicgen-small"
)

model = MusicgenForConditionalGeneration.from_pretrained(
    "facebook/musicgen-small"
)

# Input Prompt
inputs = processor(
    text=[
        "80s pop track with bassy drums and synth",
        "90s rock song with loud guitars and heavy drums"
    ],
    padding=True,
    return_tensors="pt",
)

# Generate Music
audio = model.generate(
    **inputs,
    max_new_tokens=256
)

# Sampling Rate
sampling_rate = model.config.audio_encoder.sampling_rate

# Play Audio
Audio(
    audio[0].numpy().squeeze(),
    rate=sampling_rate
)
