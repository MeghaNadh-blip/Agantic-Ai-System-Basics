import pytesseract
from PIL import Image

img = Image.open("/content/imagetext.png")

text = pytesseract.image_to_string(img)

print(text)
