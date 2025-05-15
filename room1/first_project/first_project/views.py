from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
#     return HttpResponse("This is our first home page.")



def home(request):
    return render(request, 'index.html', {'name' : 'Md. Kamrul Hasan'})