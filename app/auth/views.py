from . import auth
from flask import render_template


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "logout"


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    return render_template("sign-up")
