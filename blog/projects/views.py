from flask import Blueprint
from flask import render_template

from blog.auth import UserAwareMethodView
from blog.projects.models import Project

projects = Blueprint('projects', __name__, template_folder='templates')


class ListView(UserAwareMethodView):
    active_nav = 'projects'

    def get(self):
        context = self.get_context()
        context['projects'] = Project.objects.all()
        return render_template('projects/list.html', **context)


class DetailView(UserAwareMethodView):
    active_nav = 'projects'

    def get(self, slug):
        context = self.get_context()
        context['post'] = Project.objects.get_or_404(slug=slug)
        return render_template('posts/detail.html', **context)


# Register the urls
projects.add_url_rule('/projects/', view_func=ListView.as_view('list'))
projects.add_url_rule('/projects/<slug>/', view_func=DetailView.as_view('detail'))