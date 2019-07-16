from django.urls import path
from . import views


app_name = 'dance_School'  # here for namespacing of urls.

urlpatterns = [
    path("", views.dance_school, name="dance_school"),

]