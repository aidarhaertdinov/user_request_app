from flask import flash, url_for, redirect, render_template, request
from . import auth
from .form import LoginForm, RegistrationForm
from ..model import User
from .. import login_manager
from flask_login import login_user, logout_user, login_required
import requests
from app.repository.user_repository import user_login, user_registration, get_user


@login_manager.user_loader
def load_user(id):
    return get_user(id)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = LoginForm.form_data(form)
        user_login(user)
        return redirect(url_for("auth.success"))
        # else:
        #     flash("Вы ввели неверный адрес электронной почты или пароль", category='error')
    return render_template("auth/authorization.html", form=form, title="login")


@auth.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = RegistrationForm.form_data(form)
        user_registration(user)
        return redirect(url_for("auth.success"))
    elif request.method == 'POST':
        flash("Неверная пара логин/пароль", category='error')
    return render_template("auth/authorization.html", form=form, title="registration")


@auth.route("/logout")
# @login_required
def logout():
    logout_user()
    flash('Вы вышли из системы', category='success')
    return redirect(url_for("auth.login"))


@auth.route("/success")
# @login_required
def success():
    return render_template("auth/log_in.html", title="log in")


