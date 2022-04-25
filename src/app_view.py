from flask import Flask, request, render_template


class AppView:
    def __init__(self, explorer):
        self.supported_langs = ['ru', 'en']
        self.explorer = explorer
        self.best_lang = None
        self.app = None

    def run(self):
        self.app = Flask(__name__)

        @self.app.before_request
        def set_best_lang():
            self.best_lang = request.accept_languages.best_match(self.supported_langs)

        @self.app.route('/')
        def index():
            return render_template(f"input-form-{self.best_lang}.html")

        @self.app.route('/', methods=['POST'])
        def post_index():
            text = request.form['text']
            usages = self.explorer.get_usage(text)
            for x in usages:
                print(x)
            return render_template(f"audios-{self.best_lang}.html", data=usages, text=text)

        self.app.run()
