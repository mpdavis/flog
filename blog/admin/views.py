from flask import Blueprint, render_template, redirect, url_for, request
from flask.views import MethodView

from blog.posts.models import Post


admin = Blueprint('admin', __name__, template_folder='templates')


class EditPostView(MethodView):

    def get(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        return render_template("admin/edit-post.html", post=post)

    def post(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        title = request.form['post-title']
        body = request.form['post-body']
        post.title = title
        post.body = body
        post.save()
        return redirect(url_for('posts.detail', slug=post.slug))


class AddPostView(MethodView):

    def get(self):
        return render_template("admin/add-post.html")

    def post(self):
        post = Post(
            title=request.form.get('post-title', None),
            body=request.form.get('post-body', None),
            slug=request.form.get('post-slug', None),
        )
        post.save()
        return redirect(url_for('posts.detail', slug=post.slug))


# Register the urls
admin.add_url_rule('/admin/blog/', view_func=AddPostView.as_view('add-post'))
admin.add_url_rule('/admin/blog/<slug>/', view_func=EditPostView.as_view('edit-post'))