from . import auth
from .. import db
from flask import render_template, request, flash, redirect, url_for
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("auth/login.html")


@auth.route('/logout')
def logout():
    return "logout"


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(username) < 2:
            flash('Pick a username that is greater than 2 characters.', category='error')
        elif len(password1) < 7:
            flash('Use a stronger password that is more than 7 characters long.', category='error')
        elif password1 != password2:
            flash('Passwords did not match!!!', category='error')
        else:
            # create a new user if form is valid
            new_user = User(email=email, username=username,password=generate_password_hash(password1,method='sha256'))
            # add the new user to our db
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully.', category='success')
            return redirect(url_for('auth.login'))

    return render_template("auth/sign-up.html")

