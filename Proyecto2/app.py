from flask import Flask
from flask_cors import CORS

from controllers.users_controller import UserBlueprint

from utils.responder import respond_with_success


app = Flask(__name__)
cors = CORS(app)


# Register blueprints
app.register_blueprint(UserBlueprint)


@app.route("/")
def hello_world():
    return respond_with_success({'message': 'Hello'})





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)