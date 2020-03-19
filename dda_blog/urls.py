from django.urls import path
from . import views

app_name = 'dda_blog'  # here for namespacing of urls.

urlpatterns = [
    path("", views.dda_blog, name="dda_blog")
]
