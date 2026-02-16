from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    
    return render(request, 'index.html')
def aboutUs(request):
    return render(request, 'About.html')
def loginAt(request):
    return render(request, 'login.html')
def Products(request):
    return render(request, 'products.html')
def aboutUsDet(request, courseid):
    return HttpResponse(courseid)