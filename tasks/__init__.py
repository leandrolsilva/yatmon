from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "yatmon"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

def register_blueprints(app):
    #prevents circular imports
    from app.views import tasks
    app.register_blueprint(tasks)

register_blueprints(app)

if __name__ == '__main__':
    app.run()