from .entities.Usuario import Usuario

class ModelUsuario():
    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            # Prueba de conexión
            try:
                cursor.execute("SELECT 1")
                print("Conexión a la base de datos exitosa")
            except Exception as ex:
                print(f"Error de conexión a la base de datos: {ex}")
                return None
            # Consulta original
            sql = "SELECT * FROM usuarios WHERE username = %s"
            values = (usuario.username,)
            cursor.execute(sql, values)
            row = cursor.fetchone()
            if row != None:
                usuario_db = Usuario(row[0], row[1], Usuario.check_password(row[2], usuario.password), row[3])
                if usuario_db:
                    return usuario_db
                else:
                    return None
            else:
                return None
        except Exception as ex:
            print(f"Error en login: {ex}")
            return None
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            # Prueba de conexión
            try:
                cursor.execute("SELECT 1")
                print("Conexión a la base de datos exitosa")
            except Exception as ex:
                print(f"Error de conexión a la base de datos: {ex}")
                return None
            # Consulta original
            sql = "SELECT id, username, nombre FROM usuarios WHERE id = %s"
            values = (id,)
            cursor.execute(sql, values)
            row = cursor.fetchone()
            if row != None:
                return Usuario(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            print(f"Error en get_by_id: {ex}")
            return None     
            raise Exception(ex)