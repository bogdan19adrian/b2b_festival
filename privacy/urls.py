from django.urls import path
from . import views


app_name = 'privacy'  # here for namespacing of urls.

urlpatterns = [
    path("", views.privacy, name="privacy")
]
