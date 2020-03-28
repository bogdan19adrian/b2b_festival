from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from common.MailSenderWrapper import MailSenderWrapper
from common.common import validate_email
from dance_school.models import Carousel, DayProgram, Contact, Instructor, ProgramInterval, About

from django.views.decorators.vary import vary_on_headers

from django.views.decorators.cache import cache_control

from dda_blog.models import Post


@cache_control(private=True, max_age=3600)
@vary_on_headers('User-Agent')
def dance_school(request):
    queryset = Post.objects.filter(status=1).last()
    return render(request=request,
                  template_name='dance_school/dance_school.html',
                  context={
                      "carousel": Carousel.objects.order_by('carousel_order'),
                      "dayProgram": DayProgram.objects.all,
                      "contact": Contact.objects.last(),
                      "instructor": Instructor.objects.all,
                      "programInterval": ProgramInterval.objects.all,
                      "about": About.objects.last(),
                      "post": queryset,
                  })


def send_school_site_message(request):
    print(request)
    nameSchoolForm = request.POST['nameSchoolForm']
    emailSchoolForm = request.POST['emailSchoolForm']
    messageSchoolForm = request.POST['commentsSchoolForm']
    termsSchoolMessage = request.POST['termsSchoolMessage']
    if (validate_email(emailSchoolForm) & (termsSchoolMessage == 'false')):
        print("conditions not met")
    else:
        subject = "Mesaj de pe pagina Scolii de Dans de la " + emailSchoolForm + " " + nameSchoolForm;
        listOfRecepients = [emailSchoolForm]
        mail = MailSenderWrapper(subject, messageSchoolForm, listOfRecepients)
        mail.send_email()
    return HttpResponse("OK")
