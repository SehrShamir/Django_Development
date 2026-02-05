from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'Home PageNew'
    }
    return render(request, 'index.html', data)

def aboutUs(request):
    return HttpResponse("Welcome to wsCubeTech")
def aboutUsDet(request, courseid):
    return HttpResponse(courseid)