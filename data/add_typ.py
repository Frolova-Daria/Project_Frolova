from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddingTyp(FlaskForm):
    id = StringField('Код', validators=[DataRequired()])
    type = StringField('Вид жилья', validators=[DataRequired()])
    submit = SubmitField('Submit')