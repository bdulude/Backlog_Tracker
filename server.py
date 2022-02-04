from flask_app.controllers import routes_controller, user_controller, movies_controller
from flask_app import app
# from flask_cors import CORS, cross_origin

# app.config['CORS_HEADERS'] = 'Content-Type'
# CORS(app)

if __name__ == "__main__":
    app.run(debug=True)