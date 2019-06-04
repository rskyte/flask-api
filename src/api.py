from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "<h1>Flask API<h1>"
    
    return app

app = create_app()   