from django.contrib import admin

# Register your models here.
from dance_school.models import Instructor, Contact, ProgramInterval, DayProgram, Carousel, About

admin.site.register(Instructor)
admin.site.register(Contact)
admin.site.register(ProgramInterval)
admin.site.register(DayProgram)
admin.site.register(Carousel)
admin.site.register(About)