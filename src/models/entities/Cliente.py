class Cliente:
    def __init__(self, id, documento, tipo_documento, razon_social, telefono, email):
        self.id = id
        self.documento = documento
        self.tipo_documento = tipo_documento
        self.razon_social = razon_social
        self.telefono = telefono
        self.email = email
        self.activo = 1  # Nuevo atributo para estado activo/inactivo