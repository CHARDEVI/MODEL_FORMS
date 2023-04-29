from django.shortcuts import render
from django.http import HttpResponse
from cherry.forms import *
# Create your views here.


def insert_topic(request):
    ITO=TopicForm()
    d={'ITO':ITO}
    if request.method=="POST":
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic is inserted successfully')
        
    
    return render(request,'insert_topic.html',d)




def insert_webpage(request):
    IWO=WebpageForm()
    d={'IWO':IWO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_webpage is inserted Successfully')
    
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    IAO=AccessRecordForm()
    d={'IAO':IAO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('insert_access is inserted Successfully')
    return render(request,'insert_access.html',d)









