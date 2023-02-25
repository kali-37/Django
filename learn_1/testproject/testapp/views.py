from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

def index(requests):
    return HttpResponse("Hello world !")

def getr(request, id, name):
    return render(request, 'formfornames.html', {'id': id, 'name': name})


def checkid(request,id):
    if id==5:
        return HttpResponseNotFound(" couldn't find ")
    else:
        return HttpResponse("Your id is : {}".format(id))
