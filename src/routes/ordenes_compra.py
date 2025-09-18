from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from src.forms.orden_compra_form import OrdenCompraForm
from src.models.ModelOrdenCompra import ModelOrdenCompra
from db import db
from datetime import datetime

ordenes_compra_bp = Blueprint('ordenes_compra', __name__)

@ordenes_compra_bp.route('/ordenes_compra', methods=['GET', 'POST'])
@login_required
def index():
    form = OrdenCompraForm()
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    cursor = db.connection.cursor()
    cursor.execute('SELECT id, razon_social FROM proveedores')
    proveedores = cursor.fetchall()
    cursor.execute('SELECT id, nombre FROM productos')
    productos = cursor.fetchall()
    form.proveedor_rif.choices = [(str(p[0]), p[1]) for p in proveedores]
    for detalle_form in form.detalles:
        detalle_form.producto_codigo.choices = [(str(prod[0]), prod[1]) for prod in productos]
    if request.method == 'POST':
        print('POST data:', request.form)
        if form.validate_on_submit():
            print('Form validated:', form.data)
            detalles = []
            for detalle in form.detalles.data:
                print('Detalle:', detalle)
                detalles.append({
                    'producto_codigo': detalle['producto_codigo'],
                    'cantidad': detalle['cantidad'],
                    'precio_unitario': detalle['precio_unitario']
                })
            orden = {
                'proveedor_rif': form.proveedor_rif.data,
                'fecha': request.form.get('fecha', fecha_actual),
                'activo': 1
            }
            ModelOrdenCompra.create(orden, detalles)
            flash('Orden de compra creada exitosamente', 'success')
            return redirect(url_for('ordenes_compra.listar_ordenes'))
        else:
            print('Form errors:', form.errors)
            flash('Error en el formulario. Verifica los datos ingresados.', 'danger')
    return render_template('orden_compra/index.html', form=form, fecha_actual=fecha_actual)

@ordenes_compra_bp.route('/ordenes_compra/lista', methods=['GET'])
@login_required
def listar_ordenes():
    ordenes = ModelOrdenCompra.get_all()
    return render_template('orden_compra/lista.html', ordenes=ordenes)
