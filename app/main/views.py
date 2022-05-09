from . import main
from .. import db
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import Pitch, User
from .forms import PostForm


@main.route('/')
@login_required
def index():
    return render_template("index.html", user=current_user)


@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        content = form.content.data
        user_id = current_user._get_current_object().id
        new_pitch = Pitch(title=title, category=category, content=content, user_id=user_id)
        # new_pitch.save()
        db.session.add(new_pitch)
        db.session.commit
        return redirect(url_for('app.main.index'))
    return render_template('new_pitch.html', form=form)
