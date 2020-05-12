from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class QFlat(FlaskForm):
    ar1 = StringField('Минимальная площадь', validators=[DataRequired()])
    ar2 = StringField('Максимальная площадь', validators=[DataRequired()])
    pr1 = StringField('Минимальная цена', validators=[DataRequired()])
    pr2 = StringField('Максимальная цена', validators=[DataRequired()])
    submit = SubmitField('Submit')