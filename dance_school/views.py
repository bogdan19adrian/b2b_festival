from django.shortcuts import render

# Create your views here.
from dance_school.models import Carousel, DayProgram, Contact, Instructor, ProgramInterval, About


def dance_school(request):
    return render(request=request,
                  template_name='dance_school/dance_school.html',
                  context={
                      "carousel": Carousel.objects.all,
                      "dayProgram": DayProgram.objects.all,
                      "contact": Contact.objects.last(),
                      "instructor": Instructor.objects.all,
                      "programInterval": ProgramInterval.objects.all,
                      "about": About.objects.last(),
                           })


