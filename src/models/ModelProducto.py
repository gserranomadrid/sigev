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
    def create(self, db, producto: Producto):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO productos (codigo, nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (
                producto.get_codigo(),
                producto.get_nombre(),
                producto.get_descripcion(),
                producto.get_precio(),
                producto.get_stock()
            ))
            db.connection.commit()
            print("Producto creado correctamente")
        except Exception as ex:
            if hasattr(ex, 'args') and ex.args and '1062' in str(ex.args[0]):
                print(f"Error: Código duplicado. {ex}")
                return 'duplicado'
            print(f"Error al crear producto: {ex}")
            return 'error'

    @classmethod
    def update(self, db, producto: Producto):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE productos SET codigo=%s, nombre=%s, descripcion=%s, precio=%s, stock=%s WHERE id=%s"
            cursor.execute(sql, (
                producto.get_codigo(),
                producto.get_nombre(),
                producto.get_descripcion(),
                producto.get_precio(),
                producto.get_stock(),
                producto.get_id()
            ))
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
            cursor.execute("SELECT activo FROM productos WHERE id=%s", (id,))
            row = cursor.fetchone()
            if not row:
                print("Producto no encontrado")
                return 'error'
            estado_actual = row[0]
            nuevo_estado = 1 if estado_actual == 0 else 0
            sql = "UPDATE productos SET activo=%s WHERE id=%s"
            cursor.execute(sql, (nuevo_estado, id))
            db.connection.commit()
            print(f"Producto {'activado' if nuevo_estado == 1 else 'inactivado'} correctamente")
            return 'ok'
        except Exception as ex:
            print(f"Error al alternar estado de producto: {ex}")
            return 'error'
