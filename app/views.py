from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LTO=Webpage.objects.all()
    LTO=Webpage.objects.filter(topic_name='Cricket')   
    LTO=Webpage.objects.exclude(topic_name='Cricket')
    LTO=Webpage.objects.all()[2:5:]
    LTO=Webpage.objects.all().order_by('name')
    LTO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    LTO=Webpage.objects.all().order_by(Length('name'))
    LTO=Webpage.objects.all().order_by(Length('name').desc())
    d={'LTO':LTO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    LTO=AccessRecords.objects.all()
    d={'LTO':LTO}
    return render(request,'display_access.html',d)