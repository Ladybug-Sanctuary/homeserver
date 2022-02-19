from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Wake on LAN</h1>')
