from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddingSel(FlaskForm):
    id = StringField('Код', validators=[DataRequired()])
    fio = StringField('ФИО', validators=[DataRequired()])
    phone = StringField('Телефон', validators=[DataRequired()])
    pasport_series = StringField('Серия паспорта', validators=[DataRequired()])
    pasport_number = StringField('Номер паспорта', validators=[DataRequired()])
    submit = SubmitField('Submit')