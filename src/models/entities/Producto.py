class Producto:
    def __init__(self, id, codigo, nombre, descripcion, precio, stock, activo=1):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.activo = activo
