from django.urls import path
from . import views

app_name = 'dda_blog'  # here for namespacing of urls.

urlpatterns = [
    path("", views.PostList.as_view(), name='dekadance_blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
