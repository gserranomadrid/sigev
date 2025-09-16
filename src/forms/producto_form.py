from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange

class ProductoForm(FlaskForm):
    codigo = StringField('Código', validators=[DataRequired(), Length(max=20)])
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    descripcion = TextAreaField('Descripción', validators=[Length(max=255)])
    precio = DecimalField('Precio', validators=[DataRequired(), NumberRange(min=0)], places=2)
    stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0)])
