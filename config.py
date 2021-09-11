from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '13d9e09cbe1ea0ff77fc09d2b6e0ab43'
app.config['TEMPLATES_AUTO_RELOAD'] = True
