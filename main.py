from config import app
from views.home_controller import HomeController
from views.users_controller import UsersController
from views.events_controller import EventsController
from views.faculties_controller import FacultiesController
from views.subjects_controller import SubjectsController

if __name__ == '__main__':

    hc = HomeController()
    uc = UsersController()
    ec = EventsController()
    fc = FacultiesController()
    sc = SubjectsController
    app.run()
