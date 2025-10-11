from flask import Flask, render_template, request, redirect, url_for, flash
from .db import db
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf import CSRFProtect
from .config import config

from .routes.clientes import clientes_bp
from .routes.proveedores import proveedores_bp
from .routes.productos import productos_bp
from .routes.ordenes_compra import ordenes_compra_bp
from .routes.facturas import facturas_bp

#Modelos
from .models.ModelUsuario import ModelUsuario

#Entidades
from .models.entities.Usuario import Usuario

# La ruta a las carpetas puede necesitar ajuste si app.py está dentro de src/
# Si app.py está en src/, las rutas relativas son correctas.
app = Flask(__name__, template_folder='templates', static_folder='static')
db.init_app(app)
login_manager_app = LoginManager()
login_manager_app.init_app(app)
csrf = CSRFProtect(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUsuario.get_by_id(db, int(id))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Usuario(0, request.form['username'], request.form['password'], '')
        logged_user = ModelUsuario.login(db, user)
        if logged_user and logged_user.get_password():
            login_user(logged_user)
            return render_template('/home.html', user=logged_user)
        else:
            flash('Usuario o contraseña incorrectos', 'error')
            return render_template('auth/login.html', error="Invalid username or password")
    else:
        return render_template('auth/login.html')
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Ya no necesitas esta función aquí, las rutas de clientes están en el blueprint
# def clientes():
#     return render_template('cliente/index.html')

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    # 2. REGISTRAMOS LOS BLUEPRINTS EN LA APP
    app.register_blueprint(clientes_bp)
    app.register_blueprint(proveedores_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(ordenes_compra_bp)
    app.register_blueprint(facturas_bp)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(debug=True)
