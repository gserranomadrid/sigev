from datetime import datetime

class Factura:
    def __init__(self, id=None, cliente_id=None, fecha=None, total=0.0, estado='pendiente', detalles=None):
        self.__id = id
        self.__cliente_id = cliente_id
        self.__fecha = fecha or datetime.utcnow()
        self.__total = total
        self.__estado = estado
        self.__detalles = detalles or []

    def get_id(self):
        return self.__id
    def get_cliente_id(self):
        return self.__cliente_id
    def get_fecha(self):
        return self.__fecha
    def get_total(self):
        return self.__total
    def get_estado(self):
        return self.__estado
    def get_detalles(self):
        return self.__detalles

class DetalleFactura:
    def __init__(self, id=None, factura_id=None, producto_id=None, cantidad=0, precio_unitario=0.0):
        self.__id = id
        self.__factura_id = factura_id
        self.__producto_id = producto_id
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario

    def get_id(self):
        return self.__id
    def get_factura_id(self):
        return self.__factura_id
    def get_producto_id(self):
        return self.__producto_id
    def get_cantidad(self):
        return self.__cantidad
    def get_precio_unitario(self):
        return self.__precio_unitario
