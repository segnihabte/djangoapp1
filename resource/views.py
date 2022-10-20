from django.shortcuts import render
from django.http import HttpResponse

def names(request):
    return render(request, 'homepage.html')

def list(request, pk):
    firstnames = "abebe"
    return HttpResponse(firstnames)

def LandingPage(request):
    return render(request, 'LandingPage.html')

def listRender(request):
    list=2
    context={'list':list}
    return render(request, 'homepage.html', context)