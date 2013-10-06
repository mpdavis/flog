from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask.views import MethodView

from flask_login import login_required

from blog.auth import UserAwareMethodView
from blog.posts.models import Post


admin = Blueprint('admin', __name__, template_folder='templates')


class AdminIndexView(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_index'

    def get(self):
        context = self.get_context()
        context['posts'] = Post.objects.all()
        return render_template("admin/index.html", **context)


class EditPostView(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_edit_post'

    def get(self, slug):
        context = self.get_context()
        context['post'] = Post.objects.get_or_404(slug=slug)
        return render_template("admin/edit-post.html", **context)

    def post(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        title = request.form['post-title']
        body = request.form['post-body']
        post.title = title
        post.body = body
        post.save()
        return redirect(url_for('posts.detail', slug=post.slug))


class AddPostView(UserAwareMethodView):
    decorators = [login_required]
    active_nav = 'admin_add_post'

    def get(self):
        context = self.get_context()
        return render_template("admin/add-post.html", **context)

    def post(self):
        post = Post(
            title=request.form.get('post-title', None),
            body=request.form.get('post-body', None),
            slug=request.form.get('post-slug', None),
        )
        post.save()
        return redirect(url_for('posts.detail', slug=post.slug))


# Register the urls
admin.add_url_rule('/admin/', view_func=AdminIndexView.as_view('index'))
admin.add_url_rule('/admin/blog/', view_func=AddPostView.as_view('add-post'))
admin.add_url_rule('/admin/blog/<slug>/', view_func=EditPostView.as_view('edit-post'))