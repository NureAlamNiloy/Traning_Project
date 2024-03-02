from googletrans import Translator

def translate_to_bangla(text):
    translator = Translator()
    translation = translator.translate(text, dest='bn')  # 'bn' is the language code for Bengali
    return translation.text

if __name__ == "__main__":
    input_text = input("Enter text to translate to Bengali: ")
    translated_text = translate_to_bangla(input_text)
    print(f"Translated text: {translated_text}")
