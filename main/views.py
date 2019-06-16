from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from main.models import Carousel


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={"carousels": Carousel.objects.all})


