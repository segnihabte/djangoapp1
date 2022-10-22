from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

namesList = [
    {
        "id":'1',
        "name":"segni",
        "age":"23",
        "gender":"M",
    },
    {
        "id":'2',
        "name":"Teshome",
        "age":"30",
        "gender":"M",
    },
        {
        "id":'3',
        "name":"Habte",
        "age":"50",
        "gender":"M",
    },
]

def list(request, pk):
    firstnames = "abebe"
    return HttpResponse(firstnames)

def LandingPage(request):
    return render(request, 'LandingPage.html')

def namePro(request, pk):
    namesObj = None
    for i in namesList:
        if i["id"] == pk:
            namesObj = i
    return render(request, 'homepage.html', {'project':namesObj})
