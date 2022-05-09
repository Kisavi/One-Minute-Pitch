from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Category', choices=[('Love', 'Love'), ('Life', 'Life'), ('Motivation', 'Motivation')],
                           validators=[InputRequired()])
    content = TextAreaField('Pitch', validators=[InputRequired()])
    submit = SubmitField('Post')
