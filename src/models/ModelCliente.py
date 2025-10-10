from .entities.Cliente import Cliente
class ModelCliente():
    @classmethod
    def get_all(self, db):
        try:
            cursor = db.connection.cursor()
            # Prueba de conexión
            try:
                cursor.execute("SELECT 1")
                print("Conexión a la base de datos exitosa")
            except Exception as ex:
                print(f"Error de conexión a la base de datos: {ex}")
                return []
            # Consulta original
            sql = "SELECT id, documento, tipo_documento, razon_social, telefono, email FROM clientes"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [Cliente(*row) for row in rows]
        except Exception as ex:
            print(f"Error en get_all: {ex}")
            return []     
            raise Exception(ex)

    @classmethod
    def create(self, db, documento, tipo_documento, razon_social, telefono, email):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO clientes (documento, tipo_documento, razon_social, telefono, email) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (documento, tipo_documento, razon_social, telefono, email))
            db.connection.commit()
            print("Cliente creado correctamente")
        except Exception as ex:
            if hasattr(ex, 'args') and ex.args and '1062' in str(ex.args[0]):
                print(f"Error: Documento duplicado. {ex}")
                return 'duplicado'
            print(f"Error al crear cliente: {ex}")
            return 'error'

    @classmethod
    def update(self, db, id, documento, tipo_documento, razon_social, telefono, email):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE clientes SET documento=%s, tipo_documento=%s, razon_social=%s, telefono=%s, email=%s WHERE id=%s"
            cursor.execute(sql, (documento, tipo_documento, razon_social, telefono, email, id))
            db.connection.commit()
            print("Cliente actualizado correctamente")
            return 'ok'
        except Exception as ex:
            if hasattr(ex, 'args') and ex.args and '1062' in str(ex.args[0]):
                print(f"Error: Documento duplicado. {ex}")
                return 'duplicado'
            print(f"Error al actualizar cliente: {ex}")
            return 'error'
    @classmethod
    def inactivate(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE clientes SET activo=0 WHERE id=%s"
            cursor.execute(sql, (id,))
            db.connection.commit()
            print("Cliente inactivado correctamente")
            return 'ok'
        except Exception as ex:
            print(f"Error al inactivar cliente: {ex}")
            return 'error'