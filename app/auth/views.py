from . import auth
from flask import render_template


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "logout"


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    return "Sign up"
