from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
# from wtforms.validators import Required

class CommentForm(FlaskForm):
    comment = TextAreaField('Your comment...')
    submit = SubmitField('Submit')
