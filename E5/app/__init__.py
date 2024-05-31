from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuración de la aplicación
    app.config.from_object('config.Config')
    app.secret_key = '0011'

    # Registro de Blueprints
    from app.views.main_views import main_bp
    from app.views.auth_views import auth_bp
    from app.views.pension_views import pension_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(pension_bp)

    return app