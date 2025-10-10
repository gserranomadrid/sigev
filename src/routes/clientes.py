from flask import Blueprint, jsonify, request, render_template, current_app, flash, redirect, url_for
from ..forms.cliente_form import ClienteForm
from flask_login import login_required  # <-- 1. IMPORTAMOS login_required
from ..models.ModelCliente import ModelCliente
## No importar db ni crear un nuevo MySQL

# El Blueprint se define igual
clientes_bp = Blueprint('clientes', __name__, url_prefix='/clientes')


# 2. APLICAMOS el decorador @login_required a cada ruta que queramos proteger.
@clientes_bp.route('/', methods=['GET'])
@login_required  # <-- RUTA PROTEGIDA
def listar_clientes():
    from ..db import db
    from flask_wtf.csrf import generate_csrf
    clientes = ModelCliente.get_all(db)
    form = ClienteForm()
    csrf_token = generate_csrf()
    return render_template('cliente/index.html', clientes=clientes, form=form, csrf_token=csrf_token)

# Ruta para crear cliente
@clientes_bp.route('/crear', methods=['POST'])
@login_required
def crear_cliente():
    from ..db import db
    documento = request.form['documento']
    tipo_documento = request.form['tipo_documento']
    razon_social = request.form['razon_social']
    telefono = request.form['telefono']
    email = request.form['email']
    resultado = ModelCliente.create(db, documento, tipo_documento, razon_social, telefono, email)
    if resultado == 'duplicado':
        flash('Error: El documento ya existe en la base de datos.', 'danger')
    elif resultado == 'error':
        flash('Error al crear el cliente.', 'danger')
    else:
        flash('Cliente creado correctamente.', 'success')
    return redirect(url_for('clientes.listar_clientes'))
# Ruta para actualizar cliente
@clientes_bp.route('/actualizar', methods=['POST'])
@login_required
def actualizar_cliente():
    from ..db import db
    id = request.form['id']
    documento = request.form['documento']
    tipo_documento = request.form['tipo_documento']
    razon_social = request.form['razon_social']
    telefono = request.form['telefono']
    email = request.form['email']
    resultado = ModelCliente.update(db, id, documento, tipo_documento, razon_social, telefono, email)
    if resultado == 'duplicado':
        flash('Error: El documento ya existe en la base de datos.', 'danger')
    elif resultado == 'error':
        flash('Error al actualizar el cliente.', 'danger')
    else:
        flash('Cliente actualizado correctamente.', 'success')
    return redirect(url_for('clientes.listar_clientes'))
# Ruta para inactivar cliente
@clientes_bp.route('/inactivar/<int:id>', methods=['POST'])
@login_required
def inactivar_cliente(id):
    from ..db import db
    resultado = ModelCliente.inactivate(db, id)
    if resultado == 'ok':
        flash('Cliente inactivado correctamente.', 'success')
    else:
        flash('Error al inactivar el cliente.', 'danger')
    return redirect(url_for('clientes.listar_clientes'))