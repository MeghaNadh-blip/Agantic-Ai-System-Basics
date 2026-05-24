from googletrans import Translator

translator = Translator()

text_to_translate = "hi this is prince"

translated = translator.translate(
    text_to_translate,
    src="auto",
    dest="ko"
)

print(translated.text)
