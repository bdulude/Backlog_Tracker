from flask import Flask


app = Flask(__name__)
app.secret_key = "super secret key"

DATABASE = "backlog"

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)