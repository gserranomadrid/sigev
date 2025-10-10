from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required
from ..forms.proveedor_form import ProveedorForm
from ..models.ModelProveedor import ModelProveedor

proveedores_bp = Blueprint('proveedores', __name__, url_prefix='/proveedores')

@proveedores_bp.route('/', methods=['GET'])
@login_required
def listar_proveedores():
    from ..db import db
    from flask_wtf.csrf import generate_csrf
    proveedores = ModelProveedor.get_all(db)
    form = ProveedorForm()
    csrf_token = generate_csrf()
    return render_template('proveedor/index.html', proveedores=proveedores, form=form, csrf_token=csrf_token)

@proveedores_bp.route('/crear', methods=['POST'])
@login_required
def crear_proveedor():
    from ..db import db
    rif = request.form['rif']
    razon_social = request.form['razon_social']
    telefono = request.form['telefono']
    email = request.form['email']
    from ..models.entities.Proveedor import Proveedor
    proveedor = Proveedor(None, rif, razon_social, telefono, email)
    resultado = ModelProveedor.create(db, proveedor)
    if resultado == 'duplicado':
        flash('Error: El RIF ya existe en la base de datos.', 'danger')
    elif resultado == 'error':
        flash('Error al crear el proveedor.', 'danger')
    else:
        flash('Proveedor creado correctamente.', 'success')
    return redirect(url_for('proveedores.listar_proveedores'))

@proveedores_bp.route('/actualizar', methods=['POST'])
@login_required
def actualizar_proveedor():
    from ..db import db
    id = request.form['id']
    rif = request.form['rif']
    razon_social = request.form['razon_social']
    telefono = request.form['telefono']
    email = request.form['email']
    from ..models.entities.Proveedor import Proveedor
    proveedor = Proveedor(id, rif, razon_social, telefono, email)
    resultado = ModelProveedor.update(db, proveedor)
    if resultado == 'duplicado':
        flash('Error: El RIF ya existe en la base de datos.', 'danger')
    elif resultado == 'error':
        flash('Error al actualizar el proveedor.', 'danger')
    else:
        flash('Proveedor actualizado correctamente.', 'success')
    return redirect(url_for('proveedores.listar_proveedores'))

@proveedores_bp.route('/inactivar/<int:id>', methods=['POST'])
@login_required
def inactivar_proveedor(id):
    from ..db import db
    resultado = ModelProveedor.inactivate(db, id)
    if resultado == 'ok':
        flash('Proveedor inactivado correctamente.', 'success')
    else:
        flash('Error al inactivar el proveedor.', 'danger')
    return redirect(url_for('proveedores.listar_proveedores'))
