from django.shortcuts import render


def privacy(request):
    return render(request=request,
                  template_name='privacy/privacy.html')
