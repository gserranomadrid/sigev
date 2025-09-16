class Proveedor:
    def __init__(self, id, rif, razon_social, telefono, email, activo=1):
        self.id = id
        self.rif = rif
        self.razon_social = razon_social
        self.telefono = telefono
        self.email = email
        self.activo = activo
