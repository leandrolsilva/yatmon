from core import app

def register_blueprints(app):
    #prevents circular imports
    from tasks.views import tasks
    app.register_blueprint(tasks)

register_blueprints(app)