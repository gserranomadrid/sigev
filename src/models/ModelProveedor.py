from .entities.Proveedor import Proveedor
class ModelProveedor():
    @classmethod
    def get_all(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, rif, razon_social, telefono, email, activo FROM proveedores"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [Proveedor(*row) for row in rows]
        except Exception as ex:
            print(f"Error en get_all: {ex}")
            return []

    @classmethod
    def create(self, db, proveedor: Proveedor):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO proveedores (rif, razon_social, telefono, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (
                proveedor.get_rif(),
                proveedor.get_razon_social(),
                proveedor.get_telefono(),
                proveedor.get_email()
            ))
            db.connection.commit()
            print("Proveedor creado correctamente")
        except Exception as ex:
            if hasattr(ex, 'args') and ex.args and '1062' in str(ex.args[0]):
                print(f"Error: RIF duplicado. {ex}")
                return 'duplicado'
            print(f"Error al crear proveedor: {ex}")
            return 'error'

    @classmethod
    def update(self, db, proveedor: Proveedor):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE proveedores SET rif=%s, razon_social=%s, telefono=%s, email=%s WHERE id=%s"
            cursor.execute(sql, (
                proveedor.get_rif(),
                proveedor.get_razon_social(),
                proveedor.get_telefono(),
                proveedor.get_email(),
                proveedor.get_id()
            ))
            db.connection.commit()
            print("Proveedor actualizado correctamente")
            return 'ok'
        except Exception as ex:
            if hasattr(ex, 'args') and ex.args and '1062' in str(ex.args[0]):
                print(f"Error: RIF duplicado. {ex}")
                return 'duplicado'
            print(f"Error al actualizar proveedor: {ex}")
            return 'error'

    @classmethod
    def inactivate(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE proveedores SET activo=0 WHERE id=%s"
            cursor.execute(sql, (id,))
            db.connection.commit()
            print("Proveedor inactivado correctamente")
            return 'ok'
        except Exception as ex:
            print(f"Error al inactivar proveedor: {ex}")
            return 'error'
