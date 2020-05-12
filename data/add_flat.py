from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddingFl(FlaskForm):
    id = StringField('Код', validators=[DataRequired()])
    street = StringField('Улица', validators=[DataRequired()])
    house = StringField('Дом', validators=[DataRequired()])
    flat = StringField('Квартира', validators=[DataRequired()])
    type = StringField('Вид', validators=[DataRequired()])
    area = StringField('Площадь', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    seller = StringField('продавец', validators=[DataRequired()])
    sale = StringField('Продано', validators=[DataRequired()])
    submit = SubmitField('Submit')