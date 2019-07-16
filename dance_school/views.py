from django.shortcuts import render

# Create your views here.


def dance_school(request):
    return render(request=request,
                  template_name='dance_school/dance_school.html')