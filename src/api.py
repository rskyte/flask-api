from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>Flask API<h1>"

    @app.route("/api/users", methods=["POST"])
    def create_user():
        user_id = request.json.get('userId')
        name = request.json.get('name')
        return "User: %s, created." % user_id
    
    return app

app = create_app()   