from flask import render_template
from config import app


class EventsController(object):

    @staticmethod
    @app.route('/events/events-list')
    def events_list():
        return render_template('events/events-list.html')
