from flask import Flask
from flask_cors import CORS

from controllers.users_controller import UserBlueprint
from controllers.auth_controller import AuthBlueprint
from controllers.user.images_controller import ImageBlueprint

from utils.responder import respond_with_success
from data.seed import load_users, load_figures

app = Flask(__name__)
cors = CORS(app)


# Register seed data
load_users()
load_figures()

# Register blueprints
app.register_blueprint(UserBlueprint)
app.register_blueprint(AuthBlueprint)
app.register_blueprint(ImageBlueprint)


@app.route("/")
def hello_world():
    return respond_with_success('Welcome!!!')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)