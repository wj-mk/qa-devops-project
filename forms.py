from flask_wtf import FlaskForm
from wtforms import Stringfield, IntegerField, SubmitField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired

class Exoplanet_Form(FlaskForm):
    name = Stringfield('Planet Name', validators=[DataRequired()])
    system = StringField('System Name', validators=[DataRequired()])
    method = StringField('Discovery Method', validators=[DataRequired()])
    year = StringField('Discovery Year', validators=[DataRequired()])
    submit = SubmitField("Submit Planet")