from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", template_folder='templates/')


@app.route("/englishToFrench")
def englishToFrench():
    print("textToTranslate: ", request.args.get('textToTranslate'))
    textToTranslate = request.args.get('textToTranslate')
    return "Translated text to French: " + translator.english_to_french(textToTranslate)


@app.route("/frenchToEnglish")
def frenchToEnglish():
    print("textToTranslate: ", request.args.get('textToTranslate'))
    textToTranslate = request.args.get('textToTranslate')
    return "Translated text to English: " + translator.french_to_english(textToTranslate)


@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
