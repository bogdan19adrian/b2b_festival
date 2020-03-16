from django.db import models


# Create your models here.


class Instructor(models.Model):
    instructor_name = models.CharField(max_length=200)
    instructor_description = models.TextField()
    instructor_published = models.DateTimeField('date published')
    instructor_active = models.BooleanField()
    instructor_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.instructor_name


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_phone_number = models.CharField(max_length=20)
    contact_address = models.CharField(max_length=300)

    def __str__(self):
        return self.contact_name


class DayProgram(models.Model):
    DAYS_OF_WEEK = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    program_day = models.CharField(max_length=20, choices=DAYS_OF_WEEK)

    def __int__(self):
        print(self.program_day)
        return self.program_day

    def __str__(self):
        return str(self.program_day)


class ProgramInterval(models.Model):
    group_type = models.CharField(max_length=50)
    hour_interval = models.CharField(max_length=50)
    dance_style = models.CharField(max_length=50)
    day_program = models.ForeignKey(DayProgram, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_type


class Carousel(models.Model):
    carousel_title = models.CharField(max_length=200)
    carousel_published = models.DateTimeField('date published')
    carousel_image = models.ImageField(upload_to='images/')
    carousel_order = models.IntegerField()

    def __str__(self):
        return self.carousel_title


class About(models.Model):
    about_title = models.TextField()
    about_description = models.TextField()

    def __str__(self):
        return self.about_title
