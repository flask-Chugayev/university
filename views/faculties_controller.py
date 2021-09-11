from flask import render_template
from config import app


class FacultiesController(object):

    @staticmethod
    @app.route('/faculties/all-faculties')
    def all_faculties():
        return render_template('faculties/all-faculties.html')

    @staticmethod
    @app.route('/faculties/gryffindor')
    def gryffindor():
        return render_template('faculties/gryffindor.html')

    @staticmethod
    @app.route('/faculties/hufflepuff')
    def hufflepuff():
        return render_template('faculties/hufflepuff.html')

    @staticmethod
    @app.route('/faculties/ravenclaw')
    def ravenclaw():
        return render_template('faculties/ravenclaw.html')

    @staticmethod
    @app.route('/faculties/slytherin')
    def slytherin():
        return render_template('faculties/slytherin.html')
