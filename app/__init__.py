from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB': "yatmon"}
app.config["SECRET_KEY"] = "175V3rY53cR37B0Y"

# Settings to flask-security
app.config["SECURITY_PASSWORD_HASH"] = "sha512_crypt"
app.config["SECURITY_EMAIL_SENDER"] = "no-replay@yatmon.net"

app.config["SECURITY_POST_REGISTER_VIEW"] = "/index"

# unauthorized acess https://imgflip.com/i/6v64e
app.config["SECURITY_UNAUTHORIZED_VIEW"] = "error_403"

# mongodb connect... I'm not confident with this yet...
db = MongoEngine(app)

from app import views

if __name__ == '__main__':
    app.run()
