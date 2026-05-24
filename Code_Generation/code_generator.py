# Import Pipeline
from transformers import pipeline

# Load Model
generator = pipeline(
    "text-generation",
    model="Salesforce/codegen-350M-mono"
)

# Prompt
prompt = "write a code for even and odd"

# Generate Code
output = generator(
    prompt,
    max_length=25,
    num_return_sequences=1
)

# Print Result
print(output[0]["generated_text"])
