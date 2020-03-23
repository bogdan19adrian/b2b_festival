from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers

from .models import Post


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'dda_blog/dda_blog.html'
#
#
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = "dda_blog/dda_blog_detail.html"


# class FilteredPostList(generic.DetailView):
#     queryset = Post.objects.filter(status=1, category=1).order_by('-created_on')
@cache_control(private=True, max_age=3600)
@vary_on_headers('User-Agent')
def blog_main_mage(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    filtered_post_list = Post.objects.filter(status=1, category=1).order_by('-created_on')
    return render(request=request,
                  template_name='dda_blog/dda_blog.html',
                  context={"post_list": queryset,
                           "filtered_post_list": filtered_post_list
                           })


@cache_control(private=True, max_age=3600)
@vary_on_headers('User-Agent')
def blog_details_page(request, slug):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    # post = Post.objects.filter(title__exact=str(slug))
    post = Post.objects.all()[0]
    return render(request=request,
                  template_name='dda_blog/dda_blog_detail.html',
                  context={"post": post,
                           "post_list": post_list
                           })
