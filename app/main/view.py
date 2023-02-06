from app.main import main
from flask import render_template, request, flash, redirect, url_for
from app import login_manager
from app.model import User
from .form import UserForm
import os
# from app.auth.decorators import admin_required, user_required
from flask_login import login_required
from ..auth.view import requests

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@main.route('/')
def index():
    return render_template("main/base.html")


@main.route('/user_browser', methods=['GET'])
# @login_required
# @admin_required
def user_browser():
    users = requests.get('http://127.0.0.1:5000/rest/v1/users').json()
    return render_template("main/user_browser.html", users=users, title="Пользователи")


@main.route('/user_editor/<id>', methods=['GET', 'POST', 'PUT'])
# @login_required
def user_editor(id):
    user = requests.get(f"http://127.0.0.1:5000/rest/v1/users/{id}").json()
    if user:
        form = UserForm(id= user['id'], username=user['username'], email=user['email'], permission=user['permission'])
        if form.validate_on_submit():
            update_user = {'id': form.id.data,
                           'username': form.username.data,
                           'email': form.email.data,
                           'permission': form.permission.data}
            requests.put(f"http://127.0.0.1:5000/rest/v1/users/{id}", json=update_user)
            return redirect(url_for("main.user_browser"))
        return render_template("main/user_editor.html", form=form)


@main.route('/delete_user/<id>', methods=['GET', 'POST'])
# @login_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("main.user_browser"))