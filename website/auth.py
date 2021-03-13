from flask import Blueprint, render_template, request, flash, redirect, url_for
from .exts import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    print('add new user.')
    if request.method == 'POST':
        email = request.form.get('email')
        print(email)
        full_name = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(full_name) < 2:
            flash('Full name must be greater than 2 characters',
                  category='error')
        elif password1 != password2:
            flash('Passord don\'t match.', category='error')
        elif len(password1) < 6:
            flash('Password must be great than 5 characters.',
                  category='error')
        else:
            new_user = User(email=email,
                            full_name=full_name,
                            password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created.', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Login Success', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Wrong password, please try again!', category='error')
                return render_template('login.html')
        else:
            flash(
                'You are not an available user, please check your email address or sign up first.',
                category='error')
            return render_template('login.html')
    else:
        return render_template('login.html')
