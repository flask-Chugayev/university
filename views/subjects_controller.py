from flask import render_template
from config import app


class SubjectsController(object):

    @staticmethod
    @app.route('/subjects/all-subjects')
    def all_subjects():
        return render_template('subjects/all-subjects.html')
