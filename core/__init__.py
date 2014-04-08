from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB': "yatmon"}
app.config["SECRET_KEY"] = "175V3rY53cR37B0Y"

db = MongoEngine(app)

from core import views

if __name__ == '__main__':
    app.run()
