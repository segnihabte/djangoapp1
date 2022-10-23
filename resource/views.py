from multiprocessing import context
from django.shortcuts import render
from .models import Username
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



def naming(request):
    names = Username.objects.all()
    context={'usernames': names}
    return render(request, 'namesList.html', context)



def LandingPage(request):
    return render(request, 'LandingPage.html')

def namePro(request, pk):
    namesObj = None
    for i in namesList:
        if i["id"] == pk:
            namesObj = i
    return render(request, 'LandingPage.html', {'project':namesObj})
