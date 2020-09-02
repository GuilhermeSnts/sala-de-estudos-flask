from flask import Flask
from flask_admin import Admin

from sala_de_estudos_flask.ext.admin.lessons_admin import LessonsView
from sala_de_estudos_flask.ext.admin.professors_admin import ProfessorsView
from sala_de_estudos_flask.ext.admin.subjects_admin import SubjectsView
from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models import Subject, Professor, Lesson

admin = Admin()


def init_app(app: Flask):
    admin.name = app.config["ADMIN_NAME"]
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.url = "/admin"

    admin.add_view(ProfessorsView(Professor, db.session))

    admin.add_view(SubjectsView(Subject, db.session))

    admin.add_view(LessonsView(Lesson, db.session))
