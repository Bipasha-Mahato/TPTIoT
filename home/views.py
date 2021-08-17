from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html', {'title':'Home'})

def testpage(request):
    return render(request, 'testpage.html')

def meet(request):
    return render(request, 'meet.html', {'title':'Meet'})