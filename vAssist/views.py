from django.shortcuts import render, redirect, HttpResponse
from django.utils.html import escape
from django.utils import timezone
from django.conf import settings
from datetime import datetime
from django.core.files import File

# Create your views here.
from .forms import vQueryForm
from .models import *
import os

def assistHome(request):

    if request.method == "POST":
        media_root = str(settings.MEDIA_ROOT)
        path = media_root + "/voice-queries/"
        # userName = request.META["HTTP_USERNAME"]
        fileName = request.META["HTTP_USERNAME"] + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        extension = ".ogg"
        # print(path + fileName + extension)
        # print(fileName)
        # print(extension)

        # print(request)

        uploadedFile = open(fileName + extension, "wb+")
        myFile = File(uploadedFile)
        myFile.write(request.body)
        myFile.closed
        # print(uploadedFile)
        # print(myFile)

        # with open(path + fileName + extension, "wb+") as fo:
        #     fo.write(request.body)
        
        # put additional logic like creating a model instance or something like this here
        voiceQ = voiceQuery(audio=myFile)
        voiceQ.save()
        # return HttpResponse(escape(repr(request)))

        uploadedFile.close()
        if os.path.exists(fileName + extension):
            os.remove(fileName + extension)
        else:
            print("The file does not exist.")

        form = vQueryForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            form.save()
            return redirect('/')
    else:
        form = vQueryForm()
    return render(request, 'vAssist/assist-home.html', {'form':form})

# def upload(request):
 
#     # customHeader = request.META['HTTP_MYCUSTOMHEADER']
#     filename = "{{ user.username.title }}-"
#     # + {{ timezone.now }} + "." + e.data.type.split("/")[1]
#     # obviously handle correct naming of the file and place it somewhere like media/uploads/
#     uploadedFile = open(filename, "wb")
#     # the actual file is in request.body
#     uploadedFile.write(request.body)
#     uploadedFile.close()
#     # put additional logic like creating a model instance or something like this here
#     return HttpResponse(escape(repr(request)))