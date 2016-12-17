from django.http import HttpResponse

def hello(request,*args):
    if args:
        return HttpResponse("Hello " + args[0])
    return HttpResponse("Hello Lenovo")