from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from ..model import Permissions


class UserForm(FlaskForm):
    id = IntegerField("ID", validators=[DataRequired()], render_kw={'readonly': True})
    username = StringField("Имя пользователя: ", validators=[DataRequired()])
    email = StringField("Эл.почта: ", validators=[DataRequired()])
    permission = SelectField("Разрешение: ", choices=[e.value for e in Permissions])
    submit = SubmitField("Отправить")


    @staticmethod
    def form_data(form):
        return {'id': form.id.data,
                'username': form.username.data,
                'email': form.email.data,
                'permission': form.permission.data}

class NewUserForm(FlaskForm):

    username = StringField("Имя пользователя: ", validators=[DataRequired()])
    email = StringField("Эл.почта: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(1, 30), EqualTo('check_password')])
    check_password = PasswordField("Password: ", validators=[DataRequired(), Length(1, 30)])
    permission = SelectField("Разрешение: ", choices=[e.value for e in Permissions])
    submit = SubmitField("Отправить")

    @staticmethod
    def form_data(form):
        return {'username': form.username.data,
                'email': form.email.data,
                'password': form.password.data,
                'permission': form.permission.data}
