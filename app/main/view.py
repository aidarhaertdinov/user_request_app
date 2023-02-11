from app.main import main
from flask import render_template, request, flash, redirect, url_for
from app import login_manager
from app.model import User
from .form import UserForm
import os
# from app.auth.decorators import admin_required, user_required
from flask_login import login_required
from ..auth.view import requests
from app.repository.user_repository import get_all_users, get_user, put_user, delete_user
from app.main.form import UserForm

# @login_manager.user_loader
# def load_user(id):
#     return get_user(id)


@main.route('/')
def index():
    return render_template("main/base.html")

# TODO использовать метод из репозит слоя
@main.route('/user_browser', methods=['GET'])
# @login_required
# @admin_required
def user_browser():
    users = get_all_users()
    return render_template("main/user_browser.html", users=users, title="Пользователи")


@main.route('/user_editor/<id>', methods=['GET', 'POST', 'PUT'])
# @login_required
def user_editor(id):
    user = get_user(id)
    if user:
        form = UserForm(formdata=request.form, obj=user)
        if form.validate_on_submit():
            update_user = UserForm.form_data(form)
            put_user(id, update_user)
            return redirect(url_for("main.user_browser"))
        return render_template("main/user_editor.html", form=form)


@main.route('/delete_user/<id>', methods=['GET', 'DELETE'])
# @login_required
def user_delete(id):
    user = get_user(id)
    if user:
        delete_user(id)
        return redirect(url_for("main.user_browser"))
