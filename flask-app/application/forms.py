from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Exoplanet_Form(FlaskForm):
    name = StringField('Planet Name', validators=[DataRequired()])
    system = StringField('System Name', validators=[DataRequired()])
    method = StringField('Discovery Method', validators=[DataRequired()])
    year = IntegerField('Discovery Year', validators=[DataRequired()])
    submit = SubmitField("Submit Planet")

class EditEntry(FlaskForm):
    name = StringField('Update Planet Name')
    system = StringField('Update System Name')
    method = StringField('Update Discovery Method')
    year = IntegerField('Update Discovery Year')
    submit = SubmitField("Update Planet")

class DeleteEntry(FlaskForm):
    id = IntegerField('Provide the Exoplanet ID', validators=[DataRequired()])
    submit = SubmitField("Delete Planet")

class UpdateSelect(FlaskForm):
    id = IntegerField('Provide the Exoplanet ID', validators=[DataRequired()])
    submit = SubmitField("Select Planet")