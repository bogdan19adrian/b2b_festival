import datetime
import uuid

from django.shortcuts import render

# Create your views here.
from main.mail.MailSender import MailSender
from main.models import Carousel, ConfirmedArtists, Pricing, Ticket, Program, AboutBullet, About


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={"carousels": Carousel.objects.all,
                           "confirmed_artists": ConfirmedArtists.objects.all,
                           "pricing": Pricing.objects.all,
                           "about": About.objects.last(),
                           "about_bullet": AboutBullet.objects.all,
                           "program": Program.objects.last()
                           })


def ticketing(request):
    return render(request=request,
                  template_name='main/ticketing_system.html',
                  context={"pricing": Pricing.objects.all})


def past_edition(request):
    return render(request=request,
                  template_name='main/past_edition.html')

def buyTicket(request):
    print('tesdfsdfsfewferf')
    print(request)
    priceRon = request.POST['ron']
    priceEuro = request.POST['euro']
    email = request.POST['email']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    passType = request.POST['passType']
    code = generateShortUUID()
    ticket = Ticket.objects.create(
        ticket_priceInRon=priceRon,
        ticket_priceInEuro=priceEuro,
        ticket_email=email,
        ticket_firstName=firstName,
        ticket_lastName=lastName,
        ticket_uniqueId=code,
        ticket_dateOfPurchase=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    subject = generate_email_text(code, passType, priceEuro, priceRon)
    message = 'Thank you for joining us in this endeavour! It  means a world to us that you want to be at BtoB '
    recipient_list = [email, ]
    mail_sender = MailSender(subject, message, recipient_list)
    mail_sender.send_email()
    return render(request=request,
                  template_name='main/home.html',
                  context={"carousels": Carousel.objects.all,
                           "confirmed_artists": ConfirmedArtists.objects.all,
                           "pricing": Pricing.objects.all
                           })


def generateShortUUID():
    id = uuid.uuid4().hex[:10]
    print("idul", id)
    return id


def generate_email_text(code, ticket, euro, ron):
    message = 'Thank you for choosing to be with us. ' \
              ' You choose to purchase a  ' + ticket + ' worth ' + euro + ' EURO/' + ron + ' ron ' \
              ' In order to finalize your purchase please make the payment in the following account' \
              ' RO0000xxxxxxx - ion popescu   ' \
              ' Add in transaction comments the name, email and the following code  ' \
              + code + ' '\
              ' It is very important to add your name email and the code' \
              + code + ' in the transaction as we need them to identify you as participant with ease   ' \
              ' SEE TOU THERE!!!'
    return message
