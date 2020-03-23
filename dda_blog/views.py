from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'dda_blog/dda_blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'dda_blog/dda_blog_detail.html'
