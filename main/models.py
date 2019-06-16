from django.db import models




class Carousel(models.Model):
    carousel_title = models.CharField(max_length=200)
    carousel_content = models.TextField()
    carousel_published = models.DateTimeField('date published')
    carousel_active = models.BooleanField()
    carousel_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.carousel_title
