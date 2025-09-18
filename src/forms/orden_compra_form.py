from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FieldList, FormField, IntegerField, FloatField, HiddenField, DateField
from wtforms.validators import DataRequired, NumberRange, Email

class DetalleCompraForm(FlaskForm):
    producto_codigo = SelectField('Producto', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired(), NumberRange(min=1)])
    precio_unitario = FloatField('Precio Unitario', validators=[DataRequired(), NumberRange(min=0)])

class OrdenCompraForm(FlaskForm):
    proveedor_rif = SelectField('Proveedor', validators=[DataRequired()])
    fecha = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired()])
    detalles = FieldList(FormField(DetalleCompraForm), min_entries=1)
