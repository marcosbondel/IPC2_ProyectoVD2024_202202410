from flask import Flask
from flask_cors import CORS

from controllers.users_controller import UserBlueprint
from controllers.auth_controller import AuthBlueprint

from utils.responder import respond_with_success
from data.seed import users_list, load

app = Flask(__name__)
cors = CORS(app)


# Register seed data
load()

# Register blueprints
app.register_blueprint(UserBlueprint)
app.register_blueprint(AuthBlueprint)


@app.route("/")
def hello_world():
    return respond_with_success('Welcome')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)