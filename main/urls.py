from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("ticketing/", views.ticketing, name="ticketing"),
    path("past_editions/", views.past_edition, name="past_editions"),
    path("buyTickets", views.buyTicket, name="buyTickets"),
]