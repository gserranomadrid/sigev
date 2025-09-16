from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email

class ProveedorForm(FlaskForm):
    rif = StringField('RIF', validators=[DataRequired()])
    razon_social = StringField('Razón Social', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
