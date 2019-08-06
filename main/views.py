import datetime
import uuid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.shortcuts import render

# Create your views here.
from b2b_festival import settings
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
    message = 'Hello '+firstName + ' ' + lastName + ' Thank you for choosing to join us in this endeavour! ' \
                                                   'It  means a world to us that you want to be at BtoB '
    recipient_list = [email, ]
    mail_sender = MailSender(message,subject, recipient_list)
    # mail_sender.send_email()
    sendWithSendGrid(settings.EMAIL_HOST_USER, email, code, priceRon, priceEuro, passType, message)
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


def sendWithSendGrid(emailFrom, emailTo, code, ron, euro, ticket, message):
    message = Mail(
        from_email=emailFrom,
        to_emails=emailTo,
        subject=message,
        html_content='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> <html data-editor-version="2" class="sg-campaigns" xmlns="http://www.w3.org/1999/xhtml"> <head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" /><!--[if !mso]><!--> <meta http-equiv="X-UA-Compatible" content="IE=Edge" /><!--<![endif]--> <!--[if (gte mso 9)|(IE)]> <xml> <o:OfficeDocumentSettings> <o:AllowPNG/> <o:PixelsPerInch>96</o:PixelsPerInch> </o:OfficeDocumentSettings> </xml> <![endif]--> <!--[if (gte mso 9)|(IE)]> <style type="text/css"> body {width: 600px;margin: 0 auto;} table {border-collapse: collapse;} table, td {mso-table-lspace: 0pt;mso-table-rspace: 0pt;} img {-ms-interpolation-mode: bicubic;} </style> <![endif]--> <style type="text/css"> body, p, div { font-family: arial; font-size: 14px; } body { color: #000000; } body a { color: #1188E6; text-decoration: none; } p { margin: 0; padding: 0; } table.wrapper { width:100% !important; table-layout: fixed; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; -moz-text-size-adjust: 100%; -ms-text-size-adjust: 100%; } img.max-width { max-width: 100% !important; } .column.of-2 { width: 50%; } .column.of-3 { width: 33.333%; } .column.of-4 { width: 25%; } @media screen and (max-width:480px) { .preheader .rightColumnContent, .footer .rightColumnContent { text-align: left !important; } .preheader .rightColumnContent div, .preheader .rightColumnContent span, .footer .rightColumnContent div, .footer .rightColumnContent span { text-align: left !important; } .preheader .rightColumnContent, .preheader .leftColumnContent { font-size: 80% !important; padding: 5px 0; } table.wrapper-mobile { width: 100% !important; table-layout: fixed; } img.max-width { height: auto !important; max-width: 480px !important; } a.bulletproof-button { display: block !important; width: auto !important; font-size: 80%; padding-left: 0 !important; padding-right: 0 !important; } .columns { width: 100% !important; } .column { display: block !important; width: 100% !important; padding-left: 0 !important; padding-right: 0 !important; margin-left: 0 !important; margin-right: 0 !important; } } </style> <!--user entered Head Start--> <!--End Head user entered--> </head> <body> <center class="wrapper" data-link-color="#1188E6" data-body-style="font-size: 14px; font-family: arial; color: #000000; background-color: #ffffff;"> <div class="webkit"> <table cellpadding="0" cellspacing="0" border="0" width="100%" class="wrapper" bgcolor="#ffffff"> <tr> <td valign="top" bgcolor="#ffffff" width="100%"> <table width="100%" role="content-container" class="outer" align="center" cellpadding="0" cellspacing="0" border="0"> <tr> <td width="100%"> <table width="100%" cellpadding="0" cellspacing="0" border="0"> <tr> <td> <!--[if mso]> <center> <table><tr><td width="600"> <![endif]--> <table width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%; max-width:600px;" align="center"> <tr> <td role="modules-container" style="padding: 0px 0px 0px 0px; color: #000000; text-align: left;" bgcolor="#fcffe6" width="100%" align="left"> <table class="module preheader preheader-hide" role="module" data-type="preheader" border="0" cellpadding="0" cellspacing="0" width="100%" style="display: none !important; mso-hide: all; visibility: hidden; opacity: 0; color: transparent; height: 0; width: 0;"> <tr> <td role="module-content"> <p></p> </td> </tr> </table> <table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;"> <tr> <td style="font-size:6px;line-height:10px;padding:0px 0px 0px 0px;" valign="top" align="center"> <img class="max-width" border="0" style="display:block;color:#000000;text-decoration:none;font-family:Helvetica, arial, sans-serif;font-size:16px;max-width:100% !important;width:100%;height:auto !important;" src="https://marketing-image-production.s3.amazonaws.com/uploads/7ac67273d4e490090e0f81bf10a5623ef1b63878a1d6b128232ab78d6ffc0a90a6c012226c5cced321442934758c83a04c3e909e563a4cff5925b25e85d2cfe0.PNG" alt="" width="600"> </td> </tr> </table> <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;"> <tr> <td style="padding:18px 0px 18px 0px;line-height:22px;text-align:inherit;" height="100%" valign="top" bgcolor=""> <div> <h3 style="text-align: center;"><span style="font-family:comic sans ms,cursive;">Thank you for choosing to be with us.<br /> You choose to purchase a&nbsp; '+ticket+'&nbsp; worth&nbsp; '+euro+'&nbsp; EURO/ '+ron+' RON<br /> In order to finalize your purchase we kindly ask you to make the payment in the following account: RO0000xxxxxxx - ion popescu.</span></h3> <h3 style="text-align: center;"><span style="font-family:comic sans ms,cursive;">Add in transaction comments the name, email and the following code&nbsp; ' +code+'.</span></h3> <h3 style="text-align: center;"><span style="font-family:comic sans ms,cursive;">It is very important to add your name, your email and this code in the transaction as we need them to identify you with ease and confirm your participation.</span></h3> <h3 style="text-align: center;"><span style="font-family:comic sans ms,cursive;">SEE TOU THERE!!!</span></h3> </div> </td> </tr> </table> <table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;"> <tr> <td style="padding:0px 0px 0px 0px;" role="module-content" height="100%" valign="top" bgcolor=""> <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="10px" style="line-height:10px; font-size:10px;"> <tr> <td style="padding: 0px 0px 10px 0px;" bgcolor="#000000"></td> </tr> </table> </td> </tr> </table> <table class="module" role="module" data-type="social" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;"> <tbody> <tr> <td valign="top" style="padding:0px 0px 0px 0px;font-size:6px;line-height:10px;"> <table align="center"> <tbody> <tr> <td style="padding: 0px 5px;"> <a role="social-icon-link" href="https://www.facebook.com/bachatatakeoverbucharestdancefestival/" target="_blank" alt="Facebook" data-nolink="false" title="Facebook " style="-webkit-border-radius:2px;-moz-border-radius:2px;border-radius:2px;display:inline-block;background-color:#3B579D;"> <img role="social-icon" alt="Facebook" title="Facebook " height="30" width="30" style="height: 30px, width: 30px" src="https://marketing-image-production.s3.amazonaws.com/social/white/facebook.png" /> </a> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </td> </tr> </table> <!--[if mso]> </td></tr></table> </center> <![endif]--> </td> </tr> </table> </td> </tr> </table> </td> </tr> </table> </div> </center> </body> </html>')
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
