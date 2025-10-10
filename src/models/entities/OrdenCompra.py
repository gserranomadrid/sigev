from datetime import datetime

class OrdenCompra:
    def __init__(self, id=None, proveedor_rif=None, fecha=None, estado='activo', detalles=None):
        self.__id = id
        self.__proveedor_rif = proveedor_rif
        self.__fecha = fecha or datetime.utcnow()
        self.__estado = estado
        self.__detalles = detalles or []

    def get_id(self):
        return self.__id
    def get_proveedor_rif(self):
        return self.__proveedor_rif
    def get_fecha(self):
        return self.__fecha
    def get_estado(self):
        return self.__estado
    def get_detalles(self):
        return self.__detalles

class DetalleCompra:
    def __init__(self, id=None, cantidad=0, precio_unitario=0.0, producto_codigo=None):
        self.__id = id
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario
        self.__producto_codigo = producto_codigo

    def get_id(self):
        return self.__id
    def get_cantidad(self):
        return self.__cantidad
    def get_precio_unitario(self):
        return self.__precio_unitario
    def get_producto_codigo(self):
        return self.__producto_codigo
