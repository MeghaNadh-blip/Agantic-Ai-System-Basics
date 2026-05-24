# Install DeepFace
!pip install deepface

# Import DeepFace
from deepface import DeepFace

# Analyze Image
obj = DeepFace.analyze("/content/image2.webp")

# Print Result
print(obj)
