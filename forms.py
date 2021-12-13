from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Exoplanet_Form(FlaskForm):
    name = StringField('Planet Name', validators=[DataRequired()])
    system = StringField('System Name', validators=[DataRequired()])
    method = StringField('Discovery Method', validators=[DataRequired()])
    year = IntegerField('Discovery Year', validators=[DataRequired()])
    submit = SubmitField("Submit Planet")