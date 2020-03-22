from django.shortcuts import render


# Create your views here.


def dda_blog(request):
    return render(request=request,
                  template_name='dda_blog/dda_blog.html',
                  context={})