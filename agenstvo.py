from flask import Flask, flash, redirect, render_template, request, url_for, abort
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from data import db_session
from data import users
from data import login_form
from data import add_street, add_typ, add_seller, add_flat
from data import ul, typ, sel, flat
from data import qe_flat



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

ar1 = 0
ar2 = 200
pr1 = 0
pr2 = 10000000


class RegisterForm(FlaskForm):
    email = EmailField('Login/email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(users.User).get(user_id)


@app.route('/')
def index():
    db_session.global_init("db/rielt.db")
    session = db_session.create_session()
    ul1 = session.query(ul.Street).all()
    user = session.query(users.User).all()
    names = {name.id: (name.surname, name.name) for name in user}
    return render_template("index.html", uli=ul1, names=names, title='Агенство')


@app.route('/street')
def db_street():
    session = db_session.create_session()
    ul1 = session.query(ul.Street).all()
    user = session.query(users.User).all()
    names = {name.id: (name.surname, name.name) for name in user}
    return render_template("street.html", uli=ul1, names=names, title='База улиц')


@app.route('/type')
def db_type():
    session = db_session.create_session()
    typ1 = session.query(typ.Type).all()
    user = session.query(users.User).all()
    names = {name.id: (name.surname, name.name) for name in user}
    return render_template("type.html", typ0=typ1, names=names, title='База видов жилья')


@app.route('/seller')
def db_seller():
    session = db_session.create_session()
    sel1 = session.query(sel.Seller).all()
    user = session.query(users.User).all()
    names = {name.id: (name.surname, name.name) for name in user}
    return render_template("seller.html", sel0=sel1, names=names, title='База продавцоы')


@app.route('/flat')
def db_flat():
    session = db_session.create_session()
    flat1 = session.query(flat.Flat).all()
    user = session.query(users.User).all()
    names = {name.id: (name.surname, name.name) for name in user}
    ul1 = session.query(ul.Street).all()
    uli = {ul.id: (ul.street) for ul in ul1}
    return render_template("flat.html", flat0=flat1, names=names, uli=uli, title='База жилья')


@app.route('/q_flat', methods=['GET', 'POST'])
def q_flat():
    global ar1, ar2, pr1, pr2
    qfl = qe_flat.QFlat()
    if qfl.validate_on_submit():
        ar1 = qfl.ar1.data
        ar2 = qfl.ar2.data
        pr1 = qfl.pr1.data
        pr2 = qfl.pr2.data
        return redirect('/z_flat')
    return render_template('q_flat.html', title='Поиск предложений', form=qfl)


@app.route('/z_flat')
def db_zflat():
    session = db_session.create_session()
    flat1 = session.query(flat.Flat).filter(flat.Flat.area >= ar1, flat.Flat.area <= ar2,
                                            flat.Flat.price >= pr1, flat.Flat.price <= pr2).all()
    if flat1:
        user = session.query(users.User).all()
        names = {name.id: (name.surname, name.name) for name in user}
        ul1 = session.query(ul.Street).all()
        uli = {ul.id: (ul.street) for ul in ul1}
        return render_template("flat.html", flat0=flat1, names=names, uli=uli, title='База жилья')
    else:
        return redirect('/')
    return redirect('/')
    

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                    form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(users.User).filter(users.User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = users.User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/register')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/add_street', methods=['GET', 'POST'])
def add_st():
    adst = add_street.AddingStr()
    if adst.validate_on_submit():
        session = db_session.create_session()
        astr = ul.Street(
            id=adst.id.data,
            street=adst.street.data,
        )
        session.add(astr)
        session.commit()
        return redirect('/add_street')
    return render_template('add_street.html', title='добавление улицы', form=adst)


@app.route('/add_typ', methods=['GET', 'POST'])
def add_ty():
    adty = add_typ.AddingTyp()
    if adty.validate_on_submit():
        session = db_session.create_session()
        atyp = typ.Type(
            id=adty.id.data,
            type=adty.type.data,
        )
        session.add(atyp)
        session.commit()
        return redirect('/add_typ')
    return render_template('add_type.html', title='добавление вида жилья', form=adty)


@app.route('/add_seller', methods=['GET', 'POST'])
def add_se():
    adse = add_seller.AddingSel()
    if adse.validate_on_submit():
        session = db_session.create_session()
        asel = sel.Seller(
            id=adse.id.data,
            fio=adse.fio.data,
            phone=adse.phone.data,
            pasport_series=adse.pasport_series.data,
            pasport_number=adse.pasport_number.data,
        )
        session.add(asel)
        session.commit()
        return redirect('/add_seller')
    return render_template('add_seller.html', title='добавление продавца', form=adse)


@app.route('/add_flat', methods=['GET', 'POST'])
def add_fl():
    adfl = add_flat.AddingFl()
    if adfl.validate_on_submit():
        session = db_session.create_session()
        afl = flat.Flat(
            id = adfl.id.data,
            street = adfl.street.data,
            house = adfl.house.data,
            flat = adfl.flat.data,
            type = adfl.type.data,
            area = adfl.area.data,
            price = adfl.price.data,
            seller = adfl.seller.data,
            sale = adfl.sale.data,
        )
        session.add(afl)
        session.commit()
        return redirect('/add_flat')
    return render_template('add_flat.html', title='добавление недвижимости', form=adfl)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = login_form.LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(users.User).filter(users.User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/street_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def street_delete(id):
    session = db_session.create_session()
    street1 = session.query(ul.Street).filter(ul.Street.id == id).first()
    if street1:
        session.delete(street1)
        session.commit()
    else:
        abort(404)
    return redirect('/street')


@app.route('/typ_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def typ_delete(id):
    session = db_session.create_session()
    typ1 = session.query(typ.Type).filter(typ.Type.id == id).first()
    if typ1:
        session.delete(typ1)
        session.commit()
    else:
        abort(404)
    return redirect('/type')


@app.route('/seller_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def sel_delete(id):
    session = db_session.create_session()
    sel1 = session.query(sel.Seller).filter(sel.Seller.id == id).first()
    if sel1:
        session.delete(sel1)
        session.commit()
    else:
        abort(404)
    return redirect('/seller')


@app.route('/flat_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def flat_delete(id):
    session = db_session.create_session()
    flat1 = session.query(flat.Flat).filter(flat.Flat.id == id).first()
    if flat1:
        session.delete(flat1)
        session.commit()
    else:
        abort(404)
    return redirect('/flat')



if __name__ == "__main__":
    app.run()
