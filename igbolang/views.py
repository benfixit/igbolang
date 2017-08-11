from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'igbolang/index.html')
    #return HttpResponse("<h1>Welcome Home</h1>")
    #return render(request, 'igbolang/index.html')
