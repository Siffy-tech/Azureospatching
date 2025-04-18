# myproject/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, SAFY! How Are you today, good to have .")
