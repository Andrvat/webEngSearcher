from flask import Flask, request, render_template

supported_langs = ['ru', 'en']
app = Flask(__name__)


@app.route('/')
def index():
    best_lang = request.accept_languages.best_match(supported_langs)
    return render_template(f"input-form-{best_lang}.html")


@app.route('/', methods=['POST'])
def post_form():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text
