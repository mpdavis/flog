from flask import Blueprint
from flask import render_template

from blog.auth import UserAwareMethodView
from blog.posts.models import Post

posts = Blueprint('posts', __name__, template_folder='templates')


class ListView(UserAwareMethodView):
    active_nav = 'blog'

    def get(self, page=0):
        context = self.get_context()
        posts = Post.objects(category="blog")

        first_post = page * 3
        last_post = first_post + 3
        current_posts = posts[first_post:last_post]

        if len(posts) > last_post:
            context['older_posts'] = True
            context['next_page'] = page + 1

        context['posts'] = current_posts
        return render_template('posts/list.html', **context)


class DetailView(UserAwareMethodView):
    active_nav = 'blog'

    def get(self, slug):
        context = self.get_context()
        context['post'] = Post.objects.get_or_404(slug=slug)
        return render_template('posts/detail.html', **context)


# Register the urls
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/page/<page>', view_func=ListView.as_view('paginated'))
posts.add_url_rule('/blog/<slug>/', view_func=DetailView.as_view('detail'))