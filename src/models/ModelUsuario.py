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
            values = (usuario.get_username(),)
            cursor.execute(sql, values)
            row = cursor.fetchone()
            if row != None:
                password_valido = Usuario.check_password(row[2], usuario.get_password())
                if password_valido:
                    usuario_db = Usuario(row[0], row[1], row[2], row[3])
                    return usuario_db
                else:
                    print("Contraseña incorrecta")
                    return None
            else:
                print("Usuario no encontrado")
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