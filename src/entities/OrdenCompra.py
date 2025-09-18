from datetime import datetime

class OrdenCompra:
    def __init__(self, id=None, proveedor_rif=None, fecha=None, estado='activo', detalles=None):
        self.id = id
        self.proveedor_rif = proveedor_rif
        self.fecha = fecha or datetime.utcnow()
        self.estado = estado
        self.detalles = detalles or []

class DetalleCompra:
    def __init__(self, id=None, cantidad=0, precio_unitario=0.0, producto_codigo=None):
        self.id = id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.producto_codigo = producto_codigo
