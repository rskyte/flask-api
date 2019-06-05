import os
import sys
sys.path.append("./")
sys.path.append(os.getcwd() + "/src")

from flask import Flask, jsonify, request
from s3_logic import S3Logic

def create_app(s3_logic = S3Logic()):
    app = Flask(__name__)
    s3 = s3_logic

    @app.route("/")
    def index():
        return "<h1>Flask API<h1>"

    @app.route("/api/user/test")
    def test():
        response = s3.put({"userId": "jbloggs", "name": "Joseph Bloggs"})
        return "<h1>HELLO<h1>"

    @app.route("/api/user/new", methods=["POST"])
    def create_user():      
        try:
            user_id = request.json.get('userId')
            name = request.json.get('name')
            response = s3.put({'userId': user_id, 'name': name})
            if not response == 200:
                raise Exception      
        except Exception:
            return jsonify({'error': 'Please provide data in correct format'}), 400

        return jsonify({'status': 'success', 'userId': user_id})
    
    @app.route("/api/user/all")
    def all_users():
        users = s3.get_all_user_ids()
        return jsonify({"users": users})
    
    return app

app = create_app()   