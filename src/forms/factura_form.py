from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, FieldList, FormField, SelectField, DateField, HiddenField
from wtforms.validators import DataRequired, Optional

class DetalleFacturaForm(FlaskForm):
    producto_id = SelectField('Producto', coerce=int, validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    precio_unitario = FloatField('Precio Unitario', validators=[DataRequired()])

class FacturaForm(FlaskForm):
    cliente_id = SelectField('Cliente', coerce=int, validators=[DataRequired()])
    fecha = DateField('Fecha', validators=[Optional()])
    total = FloatField('Total', validators=[DataRequired()])
    estado = StringField('Estado', validators=[Optional()])
    detalles = FieldList(FormField(DetalleFacturaForm), min_entries=1)
