from flask import jsonify
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required
from ..models.ModelFactura import ModelFactura
from ..models.entities.Factura import Factura, DetalleFactura
from ..forms.factura_form import FacturaForm

facturas_bp = Blueprint('facturas', __name__, url_prefix='/facturas')

@facturas_bp.route('/', methods=['GET'])
@login_required
def listar_facturas():
    from ..db import db
    facturas = ModelFactura.get_all(db)
    form = FacturaForm()
    return render_template('factura/index.html', facturas=facturas, form=form)


@facturas_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear_factura():
    from ..db import db
    from ..models.ModelCliente import ModelCliente
    from ..models.ModelProducto import ModelProducto
    clientes = ModelCliente.get_all(db)
    productos = ModelProducto.get_all(db)
    form = FacturaForm()
    # Cargar opciones en los selects
    form.cliente_id.choices = [(c.get_id(), c.get_razon_social()) for c in clientes]
    for detalle_form in form.detalles:
        detalle_form.producto_id.choices = [(p.get_id(), p.get_nombre()) for p in productos]
    if request.method == 'POST':
        try:
            cliente_id = request.form['cliente_id']
            fecha = request.form.get('fecha')
            total = request.form['total']
            detalles = []
            stock_error = False
            producto_ids = request.form.getlist('producto_id[]')
            cantidades = request.form.getlist('cantidad[]')
            precios = request.form.getlist('precio_unitario[]')
            items = [
                (pid, cant, prec)
                for pid, cant, prec in zip(producto_ids, cantidades, precios)
                if pid and cant and prec
            ]
            if not items:
                flash('Debes agregar al menos un producto válido.', 'danger')
                return render_template('factura/crear.html', form=form, productos=productos)
            for pid, cant, prec in items:
                producto_id = int(pid)
                cantidad = int(cant)
                precio_unitario = float(prec)
                producto = next((p for p in productos if p.get_id() == producto_id), None)
                if producto and cantidad > producto.get_stock():
                    stock_error = True
                    flash(f'La cantidad para el producto {producto.get_nombre()} excede el stock disponible ({producto.get_stock()}).', 'danger')
                detalles.append(DetalleFactura(None, None, producto_id, cantidad, precio_unitario))
            if stock_error:
                return render_template('factura/crear.html', form=form, productos=productos)
            factura = Factura(None, cliente_id, fecha, float(total), None, detalles)
            factura_id = ModelFactura.create(db, factura)
            if factura_id:
                flash('Factura creada correctamente.', 'success')
                return redirect(url_for('facturas.listar_facturas'))
            else:
                flash('Error al crear la factura.', 'danger')
        except Exception as e:
            import traceback
            print('Error al crear la factura:', e)
            traceback.print_exc()
            flash(f'Error al crear la factura: {e}', 'danger')
            return render_template('factura/crear.html', form=form, productos=productos)
    return render_template('factura/crear.html', form=form, productos=productos)

@facturas_bp.route('/precio_producto/<int:producto_id>', methods=['GET'])
@login_required
def precio_producto(producto_id):
    from ..db import db
    from ..models.ModelProducto import ModelProducto
    productos = ModelProducto.get_all(db)
    # Buscar el producto por ID
    producto = next((p for p in productos if p.get_id() == producto_id), None)
    if producto:
        return jsonify({"precio": producto.get_precio()})
    return jsonify({"precio": None}), 404

@facturas_bp.route('/ver/<int:factura_id>', methods=['GET'])
@login_required
def ver_factura(factura_id):
    from ..db import db
    factura = ModelFactura.get_by_id(db, factura_id)
    if not factura:
        flash('Factura no encontrada.', 'danger')
        return redirect(url_for('facturas.listar_facturas'))
    return render_template('factura/detalle.html', factura=factura)
