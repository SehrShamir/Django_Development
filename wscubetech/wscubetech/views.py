from django.http import HttpResponse, HttpResponseRedirect
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

def userForm(request):
    add=0
    data={}
    
    try:
        if request.method=="POST":
            
        
            n1=int(request.POST.get('name1'))
            n2=int(request.POST.get('name2'))
            add=(n1+n2)
            data={
                'n1':n1,
                'n2':n2,
                'output':add
            }
            url="/about-us/?output={}".format(add)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request, 'userForm.html', data)