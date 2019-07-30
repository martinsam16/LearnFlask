# Aquí se definen rutas y funciones
from flask import Blueprint
from flask import render_template, request

from .forms import LoginForm

page = Blueprint('page', __name__)


@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title='404'), 404


@page.route('/')
def index():
    return render_template('index.html', title='Home')


@page.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    
    if request.method == 'POST':
        print(form.username.data)
        print(form.password.data)
        print("Nueva Sesion iniciada!")

    return render_template('auth/login.html', title='Login', form=form)
