import base64
import datetime
import os
import uuid

from django.shortcuts import render

# Create your views here.
from main.models import Carousel, ConfirmedArtists, Pricing, Ticket


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={"carousels": Carousel.objects.all,
                           "confirmed_artists": ConfirmedArtists.objects.all,
                           "pricing": Pricing.objects.all
                           })


def ticketing(request):
    return render(request=request,
                  template_name='main/ticketing_system.html',
                  context={"pricing": Pricing.objects.all})


def buyTicket(request):
    print('tesdfsdfsfewferf')
    print(request)
    priceRon = request.POST['ron']
    priceEuro = request.POST['euro']
    email = request.POST['email']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    ticket = Ticket.objects.create(
        ticket_priceInRon=priceRon,
        ticket_priceInEuro=priceEuro,
        ticket_email=email,
        ticket_firstName=firstName,
        ticket_lastName=lastName,
        ticket_uniqueId=generateShortUUID(),
        dateOfPurchase=datetime.date(datetime.now())
    )
    print(ticket)
    return render(request=request,
                  template_name='main/home.html',
                  context={"carousels": Carousel.objects.all,
                           "confirmed_artists": ConfirmedArtists.objects.all,
                           "pricing": Pricing.objects.all
                           })


def generateShortUUID():
    id = uuid.uuid4().hex[:10]
    return id;
