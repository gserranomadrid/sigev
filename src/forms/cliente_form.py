from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email

class ClienteForm(FlaskForm):
    documento = StringField('Documento', validators=[DataRequired()])
    tipo_documento = StringField('Tipo de Documento', validators=[DataRequired()])
    razon_social = StringField('Razón Social', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
