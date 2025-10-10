from .entities.Producto import Producto
class ModelProducto():
    @classmethod
    def get_all(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, codigo, nombre, descripcion, precio, stock, activo FROM productos"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [Producto(*row) for row in rows]
        except Exception as ex:
            print(f"Error en get_all: {ex}")
            return []

    @classmethod
    def create(self, db, codigo, nombre, descripcion, precio, stock):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO productos (codigo, nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (codigo, nombre, descripcion, precio, stock))
            db.connection.commit()
            print("Producto creado correctamente")
        except Exception as ex:
            if hasattr(ex, 'args') and ex.args and '1062' in str(ex.args[0]):
                print(f"Error: Código duplicado. {ex}")
                return 'duplicado'
            print(f"Error al crear producto: {ex}")
            return 'error'

    @classmethod
    def update(self, db, id, codigo, nombre, descripcion, precio, stock):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE productos SET codigo=%s, nombre=%s, descripcion=%s, precio=%s, stock=%s WHERE id=%s"
            cursor.execute(sql, (codigo, nombre, descripcion, precio, stock, id))
            db.connection.commit()
            print("Producto actualizado correctamente")
            return 'ok'
        except Exception as ex:
            if hasattr(ex, 'args') and ex.args and '1062' in str(ex.args[0]):
                print(f"Error: Código duplicado. {ex}")
                return 'duplicado'
            print(f"Error al actualizar producto: {ex}")
            return 'error'

    @classmethod
    def inactivate(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE productos SET activo=0 WHERE id=%s"
            cursor.execute(sql, (id,))
            db.connection.commit()
            print("Producto inactivado correctamente")
            return 'ok'
        except Exception as ex:
            print(f"Error al inactivar producto: {ex}")
            return 'error'
