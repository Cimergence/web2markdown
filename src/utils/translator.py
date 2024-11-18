import os, detectlanguage
from deep_translator import (GoogleTranslator,
                             DeeplTranslator,
                             )



api_key_deepl = os.getenv("DEEPL_API_KEY", "")
### to modify!!!
detectlanguage.configuration.api_key = os.getenv('SD_API_KEY', "70b5583bec3e0acf37662e4e51ccf0bd")

def lang_detection(text):
    lang = detectlanguage.detect(text)

    return lang[0]["language"]

def translate_google(text, source='auto', target='en'):
    translated = GoogleTranslator(source=source, target=target).translate(text=text)
    return translated

def translate_deepl(text, source='auto', target='en'):
    # translated = "dummy text"
    translated = DeeplTranslator(api_key=api_key_deepl, source=source, target=target, use_free_api=True).translate(text=text)
    return translated

if __name__ == "__main__":
    text = 'Keep it up. You are awesome'
    text_translated = translate_google(text, target='fr')
    print(text_translated)


