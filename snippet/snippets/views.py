from django.shortcuts import render
from django.http import HttpResponse
#from .models import Snippet

def index(request):
    #snippets = Snippet.objects.all()
   # return render(request,'index.html')
   return HttpResponse('Helloworld')


# Create your views here.
