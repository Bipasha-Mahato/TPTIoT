from django.shortcuts import render
from .models import entVideo, entNews

# Create your views here.
def entHome(request):
    entVids = reversed(entVideo.objects.all())
    entNewss = reversed(entNews.objects.all())
    return render(request, 'entCell/ent-home.html', {'entVids':entVids, 'entNewss':entNewss})