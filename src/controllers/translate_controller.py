from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel
import run_seeds 


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = query()
    if request.method == "POST":
        HistoryModel({
            "text_to_translate": request.form.get("text-to-translate"),
            "translate_from": request.form.get("translate-from"),
            "translate_to": request.form.get("translate-to")
        }).save()

        data = {
            'text_to_translate': request.form.get("text-to-translate"),
            'translate_from': request.form.get("translate-from"),
            'translate_to': request.form.get("translate-to"),
            'translated': GoogleTranslator(
                                source=request.form.get("translate-from"),
                                target=request.form.get("translate-to")).
            translate(request.form.get("text-to-translate"))
            }

        return render_template("index.html", data=data, languages=languages)

    if request.method == 'GET':
        data = {
            'text_to_translate': "O que deseja traduzir?",
            'translate_from': 'pt',
            'translate_to': 'en',
            'translated': "What do you want to translate?"
        }
        return render_template('index.html', data=data, languages=languages)


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = query()
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    inverted_translate_from = translate_to
    inverted_translate_to = translate_from

    HistoryModel({
        "text_to_translate": text_to_translate,
        "translate_from": inverted_translate_to,
        "translate_to": inverted_translate_from
    }).save()

    translated_text = GoogleTranslator(
        source=inverted_translate_from,
        target=inverted_translate_to
    ).translate(text_to_translate)

    data = {
        'text_to_translate': text_to_translate,
        'translate_from': inverted_translate_from,
        'translate_to': inverted_translate_to,
        'translated': translated_text
    }
    """ print(f"text_to_translate: {text_to_translate}")
    print(f"translate_from: {translate_from}")
    print(f"translate_to: {translate_to}")
    print(f"inverted_translate_from: {inverted_translate_from}")
    print(f"inverted_translate_to: {inverted_translate_to}")
    print(f"translated_text: {translated_text}") """

    return render_template("index.html", data=data, languages=languages)


def query():
    run_seeds.seed_language()
    languages = LanguageModel.list_dicts()
    obj = []
    for lingua in languages:
        if lingua['name'] == 'portuguese':
            lingua['name'] = 'PORTUGUES'
            obj.append(lingua)
        else:
            obj.append(lingua)
    return obj
