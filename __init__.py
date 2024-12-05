from flask import Flask
from controllers.content import content

def create_app():
    app = Flask(__name__)
    
    app_name = [
        content,
    ]

    for i in app_name:
        app.register_blueprint(i)
    
    return app