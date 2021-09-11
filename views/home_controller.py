from flask import render_template
from config import app


class HomeController(object):

    @staticmethod
    @app.route('/home/contact')
    def contact():
        return render_template('home/contact.html')

    @staticmethod
    @app.route('/')
    def index():
        return render_template('home/index.html')
