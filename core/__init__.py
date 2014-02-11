from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "yatmon"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

from core import views

if __name__ == '__main__':
    app.run()