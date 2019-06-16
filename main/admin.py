from django.contrib import admin


# Register your models here.
from main.models import Carousel, ConfirmedArtists

admin.site.register(Carousel)
admin.site.register(ConfirmedArtists)