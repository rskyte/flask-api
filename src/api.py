from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>Flask API<h1>"

    @app.route("/api/users", methods=["POST"])
    def create_user():
        try:
            user_id = request.json.get('userId')
            name = request.json.get('name')
        except Exception:
            return jsonify({'error': 'Please provide data in correct format'}), 400

        return jsonify({'status': 'success', 'userId': user_id})
    
    return app

app = create_app()   