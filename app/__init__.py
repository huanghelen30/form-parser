from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    # Register Blueprints or routes
    from app.routes import main
    app.register_blueprint(main)

    # Optional: init DB
    # init_db(app)

    return app
