from django.contrib import admin


# Register your models here.
from main.models import Carousel, ConfirmedArtists, Pricing

admin.site.register(Carousel)
admin.site.register(ConfirmedArtists)
admin.site.register(Pricing)