from flask import Flask, request, render_template


class AppView:
    def __init__(self, explorer, supported_langs=None):
        if supported_langs is None:
            supported_langs = ['ru', 'en']
        self.explorer = explorer
        self.supported_langs = supported_langs

    def run(self):
        app = Flask(__name__)

        @app.route('/')
        def index():
            best_lang = request.accept_languages.best_match(self.supported_langs)
            return render_template(f"input-form-{best_lang}.html")

        @app.route('/', methods=['POST'])
        def post_index():
            text = request.form['text']
            print(self.explorer.get_usage(text))
            return render_template("audios.html")

        app.run()
