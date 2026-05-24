import pytesseract
from PIL import Image

# Load Image
img = Image.open("/content/imagetext.png")

# Extract Text
text = pytesseract.image_to_string(img)

# Print Output
print(text)
