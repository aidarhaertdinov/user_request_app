from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from enum import Enum
# from ..model import Permissions


class UserForm(FlaskForm):
    id = IntegerField("№", validators=[DataRequired()])
    user_name = StringField("Имя пользователя: ", validators=[DataRequired()])
    permission = SelectField("Разрешение: ") #, choices=[e.value for e in Permissions]
    submit = SubmitField("Отправить")