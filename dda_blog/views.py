from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers

from .models import Post


# @cache_control(private=True, max_age=3600)
# @vary_on_headers('User-Agent')
def blog_main_mage(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    filtered_post_list = Post.objects.filter(status=1, category=1).order_by('-created_on')

    paginator = Paginator(queryset, 10) # Show 10 Posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request=request,
                  template_name='dda_blog/dda_blog.html',
                  context={"filtered_post_list": filtered_post_list, 'page_obj': page_obj
                           })


# @cache_control(private=True, max_age=3600)
# @vary_on_headers('User-Agent')
def blog_details_page(request, slug):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    post = Post.objects.get(slug=slug)
    # post = Post.objects.all()[0]
    return render(request=request,
                  template_name='dda_blog/dda_blog_detail.html',
                  context={"post": post,
                           "post_list": post_list
                           })
