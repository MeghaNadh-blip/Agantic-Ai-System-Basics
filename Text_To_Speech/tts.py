from gtts import gTTS
from IPython.display import Audio

text = input("Enter Your Text: ")

tts = gTTS(text=text, lang="en", tld="co.in", slow=True)
tts.save("output.mp3")

Audio("output.mp3", autoplay=True)
