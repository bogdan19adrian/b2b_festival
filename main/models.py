from django.db import models


class Carousel(models.Model):
    carousel_title = models.CharField(max_length=200)
    carousel_content = models.TextField()
    carousel_published = models.DateTimeField('date published')
    carousel_active = models.BooleanField()
    carousel_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.carousel_title


class ConfirmedArtists(models.Model):
    confirmedArtists_name = models.CharField(max_length=200)
    confirmedArtists_description = models.TextField()
    confirmedArtists_published = models.DateTimeField('date published')
    confirmedArtists_active = models.BooleanField()
    confirmedArtists_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.confirmedArtists_name


class Pricing(models.Model):
    pricing_price = models.CharField(max_length=50)
    pricing_type = models.CharField(max_length=200)
    pricing_details = models.TextField()
    pricing_published = models.DateTimeField('date published')
    pricing_active = models.BooleanField()
    pricing_image = models.ImageField(upload_to='images/')
    pricing_price_EURO = models.IntegerField()
    pricing_price_LEU = models.IntegerField()

    def __str__(self):
        return self.pricing_price


class Ticket(models.Model):
    ticket_priceInRon = models.IntegerField()
    ticket_priceInEuro = models.IntegerField()
    ticket_email = models.EmailField()
    ticket_firstName = models.CharField(max_length=200)
    ticket_lastName = models.CharField(max_length=200)
    ticket_uniqueId = models.CharField(max_length=200)
    ticket_dateOfPurchase = models.DateTimeField('date published')

    def __str__(self):
        return self.ticket_uniqueId


class About(models.Model):
    about_title = models.TextField()
    about_description = models.TextField()

    def __str__(self):
        return self.about_title


class AboutBullet(models.Model):
    about_bullet_title = models.CharField(max_length=200)
    about_bullet_description = models.CharField(max_length=500)
    about_bullet_icon = models.CharField(max_length=500)

    def __str__(self):
        return self.about_bullet_title


class Program(models.Model):
    program_title = models.CharField(max_length=50)
    program_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.program_title


class PaymentOption(models.Model):
    paymentType = models.CharField(max_length=50, primary_key=True)
    account_owner = models.CharField(max_length=50)
    account_number = models.CharField(max_length=100)

    def __str__(self):
        return self.paymentType


class ConfirmedPhoto(models.Model):
    confirmedPhoto_name = models.CharField(max_length=200)
    confirmedPhoto_description = models.TextField()
    confirmedPhoto_published = models.DateTimeField('date published')
    confirmedPhoto_active = models.BooleanField()
    confirmedPhoto_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.confirmedPhoto_name


class ConfirmedDJs(models.Model):
    confirmedDJs_name = models.CharField(max_length=200)
    confirmedDJs_description = models.TextField()
    confirmedDJs_published = models.DateTimeField('date published')
    confirmedDJs_active = models.BooleanField()
    confirmedDJs_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.confirmedDJs_name
