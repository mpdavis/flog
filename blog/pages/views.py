from flask import Blueprint, render_template
from flask.views import MethodView

from blog.posts.models import Post

pages = Blueprint('pages', __name__, template_folder='templates')


class ProjectsView(MethodView):

    def get(self):
        return render_template('pages/projects.html')


class ResumeView(MethodView):

    def get(self):
        return render_template('pages/resume.html')


# Register the urls
pages.add_url_rule('/projects/', view_func=ProjectsView.as_view('projects'))
pages.add_url_rule('/resume/', view_func=ResumeView.as_view('resume'))
