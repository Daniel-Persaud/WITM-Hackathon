from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from safeto.models import Report

class ReportForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired()])
    location = TextAreaField('Location', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit Report')