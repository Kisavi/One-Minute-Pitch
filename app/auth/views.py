from . import auth
from flask import render_template, request


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("auth/login.html")


@auth.route('/logout')
def logout():
    return "logout"


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    return render_template("auth/sign-up.html")
