from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from safeto.models import Post

class ReportForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    location = TextAreaField('Location', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit Report')