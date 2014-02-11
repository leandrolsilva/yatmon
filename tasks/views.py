from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from app.models import Task

tasks = Blueprint('tasks',__name__, template_folder='templates')


class ListView(MethodView):

    def get(self):
        tasks = Task.objects.all()
        return render_template('tasks/list.html', tasks=tasks)


class DetailView(MethodView):

    def get(selfi, slug):
        task = Task.objects.get_or_404(slug=slug)
        return render_template('tasks/task.html', task=task)

# Register the urls
tasks.add_url_rule('/tasks/', view_func=ListView.as_view('list'))
tasks.add_url_rule('/<slug>/', view_func=DetailView.as_view('task'))
