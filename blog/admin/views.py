from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from flask_login import login_required

from markdown import markdown

from blog import db

from blog.auth import UserAwareMethodView
from blog.admin.forms import NewPostForm
from blog.admin.forms import NewProjectForm
from blog.posts.models import Post
from blog.projects.models import Project


admin = Blueprint('admin', __name__, template_folder='templates')


class AdminIndexView(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_index'

    def get(self):
        context = self.get_context()
        context['full_width'] = True
        return render_template("admin/index.html", **context)


class AdminPosts(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_posts'

    def get(self):
        context = self.get_context()
        context['posts'] = Post.objects.all()
        return render_template("admin/posts.html", **context)


class AdminViewPost(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_posts'

    def get(self, slug):
        context = self.get_context()
        context['posts'] = Post.objects.all()
        context['current_post'] = Post.objects.get_or_404(slug=slug)
        return render_template("admin/posts.html", **context)


class AdminProjects(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_projects'

    def get(self):
        context = self.get_context()
        context['projects'] = Project.objects.all()
        return render_template("admin/projects.html", **context)


class AdminEditPost(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_edit_post'

    def get(self, slug):
        context = self.get_context()
        post = Post.objects.get_or_404(slug=slug)

        form = NewPostForm()
        form.title.data = post.title
        form.slug.data = post.slug
        form.body.data = post.markdown_body

        context['form'] = form
        context['post'] = post
        context['full_width'] = True
        return render_template("admin/edit-post.html", **context)

    def post(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        title = request.form['title']
        markdown_body = request.form['body']
        post.title = title
        post.markdown_body = markdown_body
        post.html_body = markdown(markdown_body)
        post.save()
        return redirect(url_for('posts.detail', slug=post.slug))


class EditProjectView(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_edit_project'

    def get(self, slug):
        context = self.get_context()
        context['form'] = NewPostForm(title="test")
        context['project'] = Project.objects.get_or_404(slug=slug)
        return render_template("admin/edit-project.html", **context)

    def post(self, slug):
        project = Project.objects.get_or_404(slug=slug)
        title = request.form['title']
        body = request.form['body']
        project.title = title
        project.body = body
        project.save()
        return redirect(url_for('posts.detail', slug=project.slug))


class AdminAddPost(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_add_post'

    def get(self):
        context = self.get_context()
        context['form'] = NewPostForm()
        context['full_width'] = True
        return render_template("admin/add-post.html", **context)

    def post(self):
        post = Post(
            title=request.form.get('title', None),
            markdown_body=request.form.get('body', None),
            html_body=markdown(request.form.get('body', None)),
            slug=request.form.get('slug', None),
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.detail', slug=post.slug))


class AddProjectView(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_add_project'

    def get(self):
        context = self.get_context()
        context['form'] = NewProjectForm()
        return render_template("admin/add-project.html", **context)

    def post(self):
        project = Project(
            title=request.form.get('title', None),
            subtitle=request.form.get('subtitle', None),
            body=request.form.get('body', None),
            slug=request.form.get('slug', None),
        )
        project.save()
        return redirect(url_for('projects.detail', slug=project.slug))


class AdminSettings(UserAwareMethodView):
    decorators = [login_required]
    active_nav = "admin_settings"

    def get(self):
        context = self.get_context()
        return render_template("admin/settings.html", **context)


# Register the urls
admin.add_url_rule('/admin/', view_func=AdminIndexView.as_view('index'))
admin.add_url_rule('/admin/posts/', view_func=AdminPosts.as_view('posts'))
admin.add_url_rule('/admin/posts/new/', view_func=AdminAddPost.as_view('add-post'))
admin.add_url_rule('/admin/posts/<slug>/', view_func=AdminViewPost.as_view('view-post'))
admin.add_url_rule('/admin/posts/<slug>/edit', view_func=AdminEditPost.as_view('edit-post'))

admin.add_url_rule('/admin/projects/', view_func=AdminProjects.as_view('projects'))
admin.add_url_rule('/admin/project/', view_func=AddProjectView.as_view('add-project'))
admin.add_url_rule('/admin/project/<slug>', view_func=EditProjectView.as_view('edit-project'))

admin.add_url_rule('/admin/settings/', view_func=AdminSettings.as_view('settings'))

