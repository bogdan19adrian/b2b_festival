from django.urls import path
from . import views

app_name = 'dda_blog'  # here for namespacing of urls.

urlpatterns = [
    path("", views.blog_main_mage, name='dekadance_blog'),
    path('<slug:slug>/', views.blog_details_page, name='post_detail'),

]
