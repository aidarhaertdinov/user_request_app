from app.main import main
from flask import render_template, request, flash, redirect, url_for
from app import login_manager
# from flask_wtf.csrf import CSRFError
# from app.model import ProductLine, db, User
from .form import UserForm
import os
# from app.auth.decorators import admin_required, user_required
from flask_login import login_required


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@main.route('/')
def index():
    return render_template("main/base.html")


@main.route('/user_browser')
# @login_required
# @admin_required
def user_browser():
    users = User.query.all()
    return render_template("main/user_browser.html", users=users, title="Пользователи")


@main.route('/user_editor/<id>', methods=['GET', 'POST'])
# @login_required
def user_editor(id):
    user = User.query.filter_by(id=id).first()
    if user:
        form = UserForm(formdata=request.form, obj=user)
        if form.validate_on_submit():
            user.id = form.id.data
            user.user_name = form.user_name.data
            user.permission = form.permission.data
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("main.user_browser"))
        return render_template("main/user_editor.html", form=form)


@main.route('/delete_user/<id>', methods=['GET', 'POST'])
# @login_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("main.user_browser"))