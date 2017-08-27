from django.http import  HttpResponse

def index(request):
    return HttpResponse("<h1>PDF Generatr Data Form</h1>")