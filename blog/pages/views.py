from flask import Blueprint
from flask import render_template

from blog.auth import UserAwareMethodView
from blog.posts.models import Post

pages = Blueprint('pages', __name__, template_folder='templates')


class ProjectsView(UserAwareMethodView):
    active_nav = "pages_projects"

    def get(self):
        context = self.get_context()
        return render_template('pages/projects.html', **context)


class ResumeView(UserAwareMethodView):
    active_nav = "pages_resume"

    def get(self):
        context = self.get_context()
        return render_template('pages/resume.html', **context)


# Register the urls
pages.add_url_rule('/projects/', view_func=ProjectsView.as_view('projects'))
pages.add_url_rule('/resume/', view_func=ResumeView.as_view('resume'))
