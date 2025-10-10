from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required
from ..forms.producto_form import ProductoForm
from ..models.ModelProducto import ModelProducto

productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

@productos_bp.route('/', methods=['GET'])
@login_required
def listar_productos():
    from ..db import db
    from flask_wtf.csrf import generate_csrf
    productos = ModelProducto.get_all(db)
    form = ProductoForm()
    csrf_token = generate_csrf()
    return render_template('producto/index.html', productos=productos, form=form, csrf_token=csrf_token)

@productos_bp.route('/crear', methods=['POST'])
@login_required
def crear_producto():
    from ..db import db
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    stock = request.form['stock']
    resultado = ModelProducto.create(db, codigo, nombre, descripcion, precio, stock)
    if resultado == 'duplicado':
        flash('Error: El código ya existe en la base de datos.', 'danger')
    elif resultado == 'error':
        flash('Error al crear el producto.', 'danger')
    else:
        flash('Producto creado correctamente.', 'success')
    return redirect(url_for('productos.listar_productos'))

@productos_bp.route('/actualizar', methods=['POST'])
@login_required
def actualizar_producto():
    from ..db import db
    id = request.form['id']
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    stock = request.form['stock']
    resultado = ModelProducto.update(db, id, codigo, nombre, descripcion, precio, stock)
    if resultado == 'duplicado':
        flash('Error: El código ya existe en la base de datos.', 'danger')
    elif resultado == 'error':
        flash('Error al actualizar el producto.', 'danger')
    else:
        flash('Producto actualizado correctamente.', 'success')
    return redirect(url_for('productos.listar_productos'))

@productos_bp.route('/inactivar/<int:id>', methods=['POST'])
@login_required
def inactivar_producto(id):
    from ..db import db
    resultado = ModelProducto.inactivate(db, id)
    if resultado == 'ok':
        flash('Producto inactivado correctamente.', 'success')
    else:
        flash('Error al inactivar el producto.', 'danger')
    return redirect(url_for('productos.listar_productos'))
