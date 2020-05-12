from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddingStr(FlaskForm):
    id = StringField('Код', validators=[DataRequired()])
    street = StringField('Улица', validators=[DataRequired()])
    submit = SubmitField('Submit')