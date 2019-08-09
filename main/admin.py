from django.contrib import admin

# Register your models here.
from main.models import Carousel, ConfirmedArtists, Pricing, Ticket, Program, AboutBullet, About, PaymentOption, \
    ConfirmedPhoto, ConfirmedDJs

admin.site.register(Carousel)
admin.site.register(ConfirmedArtists)
admin.site.register(Pricing)
admin.site.register(Ticket)
admin.site.register(AboutBullet)
admin.site.register(Program)
admin.site.register(About)
admin.site.register(PaymentOption)
admin.site.register(ConfirmedPhoto)
admin.site.register(ConfirmedDJs)

