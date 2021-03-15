from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .exts import db
from .models import User, Program
from datetime import date, datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html")


@views.route('/edit-program', methods=['GET', 'POST'])
def edit_program():
    programs = Program.query.all()

    return render_template("manage.html", programs=programs)


@views.route('/add-program', methods=['GET', 'POST'])
def add_program():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        hold_date = request.form.get('hold_date')
        frequency = request.form.get('frequency')
        participants_No = request.form.get('participants_No')
        participants_group = request.form.get('participants_group')
        duration = request.form.get('duration')
        status = request.form.get('status')

        # user = User.query.filter_by(email=email).first()
        # if user:
        #     flash('Email already exists.', category='error')
        # elif len(email) < 4:
        #     flash('Email must be greater than 3 characters.', category='error')
        # elif len(full_name) < 2:
        #     flash('Full name must be greater than 2 characters',
        #           category='error')
        # elif password1 != password2:
        #     flash('Passord don\'t match.', category='error')
        # elif len(password1) < 6:
        #     flash('Password must be great than 5 characters.',
        #           category='error')
        # else:
        new_program = Program(title=title,
                              content=content,
                              hold_date=datetime.strptime(
                                  hold_date, '%Y-%m-%d'),
                              frequency=frequency,
                              participants_No=participants_No,
                              participants_group=participants_group,
                              duration=duration,
                              status=status,
                              created_by=current_user.id)
        db.session.add(new_program)
        db.session.commit()
        flash('Account created.', category='success')
        return redirect(url_for('views.edit_program'))

    return render_template("add_program.html")
