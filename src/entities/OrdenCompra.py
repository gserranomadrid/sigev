from datetime import datetime

class OrdenCompra:
    def __init__(self, id=None, proveedor_rif=None, fecha=None, estado='activo', detalles=None):
        self.__id = id
        self.__proveedor_rif = proveedor_rif
        self.__fecha = fecha or datetime.utcnow()
        self.__estado = estado
        self.__detalles = detalles or []

class DetalleCompra:
    def __init__(self, id=None, cantidad=0, precio_unitario=0.0, producto_codigo=None):
        self.__id = id
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario
        self.__producto_codigo = producto_codigo
