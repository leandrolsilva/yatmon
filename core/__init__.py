from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "yatmon"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

#Settings to flask-security
#define the hash alg.
app.config["SECURITY_PASSWORD_HASH"] = "sha512_crypt"

#define the fake email (e.g notification of a active task)
app.config["SECURITY_EMAIL_SENDER"] = "no-replay@yatmon.net"
app.config["SECURITY_LOGIN_URL"] = "/signin"
app.config["SECURITY_LOGOUT_URL"] = "/logout"
app.config["SECURITY_REGISTER_URL"] = "/signup"
app.config["SECURITY_POST_REGISTER_VIEW"] = "/index"

#unauthorized acess https://imgflip.com/i/6v64e
app.config["SECURITY_UNAUTHORIZED_VIEW"] = "error_403"

#login user template
app.config["SECURITY_LOGIN_USER_TEMPLATE"] = "signin.html"

app.config["SECURITY_REGISTER_USER_TEMPLATE"] = "signup.html"
app.config[] = ""
app.config[] = ""
app.config[] = ""
app.config[] = ""

#mongo connect
db = MongoEngine(app)

from core import views

if __name__ == '__main__':
    app.run()
