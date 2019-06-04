from flask import Flask
app = Flask(__name__)

#def create_app():
    #app = Flask(__name__)
    #return app
    
@app.route("/")
def hello():
    return "Hello World v2!"

    