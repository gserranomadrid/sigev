# Sistema de Gestión de Ventas (SIGEV)

Este es un sistema de gestión de ventas desarrollado en Python con el framework Flask y MySQL como base de datos.

## Prerrequisitos

Antes de comenzar, asegúrate de tener instalado el siguiente software en tu sistema:

  * Python 3.x
  * Git
  * MySQL (se recomienda [XAMPP](https://www.apachefriends.org/index.html) para usuarios de Windows)

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local.

**1. Clonar el repositorio** 

Primero, clona el repositorio desde GitHub y accede a la carpeta del proyecto.

```bash
git clone https://github.com/gserranomadrid/sigev.git
cd sigev
```

**2. Crear y activar el entorno virtual** 

Crea un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv venv
```

Luego, activa el entorno

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1
```

**3. Instalar dependencias**

Instala todas las librerías y paquetes necesarios que se encuentran en el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

**4. Configurar la base de datos**

  * Asegúrate de que tu servidor MySQL esté en funcionamiento.

  * Crea una base de datos y un usuario en MySQL. Puedes utilizar el archivo `.sql` proporcionado para importar la estructura y los datos iniciales.

  * Edita el archivo `src/config.py` con tus credenciales de conexión a la base de datos (host, usuario, contraseña y nombre de la base de datos).

    ```python
    # src/config.py

    class DevelopmentConfig(Config):
        DEBUG = True
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'tu_usuario'      # Cambia esto
        MYSQL_PASSWORD = 'tu_contraseña' # Cambia esto
        MYSQL_DB = 'nombre_de_tu_bd' # Cambia esto
    ```

**5. Ejecutar la aplicación** 

Una vez que todo esté configurado, inicia el servidor de desarrollo de Flask con el siguiente comando:

```bash
python -m src.app
```

**6. Acceder a la aplicación** 

Abre tu navegador web y visita la siguiente URL para ver la aplicación en funcionamiento:
[http://localhost:5000](https://www.google.com/search?q=http://localhost:5000)
