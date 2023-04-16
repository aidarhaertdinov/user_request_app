from .. import login_manager
from app.main import main
from flask import render_template, request, redirect, url_for, current_app
from app.main.form import UserForm, NewUserForm



@login_manager.user_loader
def load_user(id: int):

    return get_user(id)


@main.route('/')
def index():
    from main import app
    user = {'email': current_app.config.get('ADMIN_EMAIL'),
            'password': current_app.config.get('ADMIN_PASSWORD')
            }
    app.user_repository.user_login(user)


    return render_template("main/base.html")


@main.route("/create_user", methods=['GET', 'POST'])
def create_user():
    from main import app

    form = NewUserForm()
    if form.validate_on_submit():
        user = NewUserForm.form_data(form)
        app.user_repository.create_user(user)
        return redirect(url_for("main.user_browser"))
    elif request.method == 'POST':
        flash("Неверная пара логин/пароль", category='error')

    return render_template("main/user_create.html", form=form)



@main.route('/user_browser', methods=['GET'])
def user_browser():
    from main import app

    users = app.user_repository.get_users()

    return render_template("main/user_browser.html", users=users, title="Пользователи")


@main.route('/user_editor/<id>', methods=['GET', 'POST', 'PUT'])
def user_editor(id):
    from main import app

    user = app.user_repository.get_user(id)
    if user:
        form = UserForm(formdata=request.form, obj=user)
        if form.validate_on_submit():
            update_user = UserForm.form_data(form)
            app.user_repository.put_user(id, update_user)

            return redirect(url_for("main.user_browser"))

        return render_template("main/user_editor.html", form=form)


@main.route('/delete_user/<id>', methods=['GET', 'DELETE'])
def user_delete(id):
    from main import app

    user = app.user_repository.get_user(id)
    if user:
        app.user_repository.delete_user(id)

        return redirect(url_for("main.user_browser"))
