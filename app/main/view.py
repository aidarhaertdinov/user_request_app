from .. import login_manager
from app.main import main
from flask import render_template, request, redirect, url_for
from app.repository.user_repository import UserRepository
from app.main.form import UserForm, NewUserForm
from config import Config


@login_manager.user_loader
def load_user(id):
    return get_user(id)

@main.route('/', methods=['GET', 'POST'])
def index():
    user = {'email': Config.ADMIN_EMAIL,
            'password': Config.ADMIN_PASSWORD
            }
    UserRepository.user_login(user)
    return render_template("main/base.html")


@main.route("/create_user", methods=['GET', 'POST'])
def create_user():
    form = NewUserForm()
    if form.validate_on_submit():
        user = NewUserForm.form_data(form)
        UserRepository.create_user(user)
        return redirect(url_for("main.user_browser"))
    elif request.method == 'POST':
        flash("Неверная пара логин/пароль", category='error')
    return render_template("main/user_create.html", form=form)


@main.route('/user_browser', methods=['GET'])
def user_browser():
    users = UserRepository.get_all_users()
    return render_template("main/user_browser.html", users=users, title="Пользователи")


@main.route('/user_editor/<id>', methods=['GET', 'POST', 'PUT'])
def user_editor(id):
    user = UserRepository.get_user(id)
    if user:
        form = UserForm(formdata=request.form, obj=user)
        if form.validate_on_submit():
            update_user = UserForm.form_data(form)
            UserRepository.put_user(id, update_user)
            return redirect(url_for("main.user_browser"))
        return render_template("main/user_editor.html", form=form)


@main.route('/delete_user/<id>', methods=['GET', 'DELETE'])
def user_delete(id):
    user = UserRepository.get_user(id)
    if user:
        UserRepository.delete_user(id)
        return redirect(url_for("main.user_browser"))
