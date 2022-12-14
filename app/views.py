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
    LTO=Webpage.objects.all()
    LTO=Webpage.objects.filter(name__startswith='s')
    LTO=Webpage.objects.filter(name__endswith='a')
    LTO=Webpage.objects.filter(name__contains='a')
    LTO=Webpage.objects.filter(name__in='rajitha')
    LTO=Webpage.objects.filter(name__regex='^m')
    LTO=Webpage.objects.filter(name__in=('rajitha','mahi'))
    d={'LTO':LTO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    LTO=AccessRecords.objects.all()
    LTO=AccessRecords.objects.filter(date='2022-12-1')
    LTO=AccessRecords.objects.filter(date__gt='2021-6-14')
    LTO=AccessRecords.objects.filter(date__year='2021')
    LTO=AccessRecords.objects.filter(date__month='5')
    LTO=AccessRecords.objects.filter(date__day='22') 
    LTO=AccessRecords.objects.filter(date__day__gt='6')
    LTO=AccessRecords.objects.filter(date__year__gt='2021')
    LTO=AccessRecords.objects.filter(date__month__gt='5')
    LTO=AccessRecords.objects.filter(date__day__gte='6')  
    LTO=AccessRecords.objects.filter(date__lt='2021-6-14')
    LTO=AccessRecords.objects.filter(date__day__lt='6')   
    LTO=AccessRecords.objects.filter(date__year__lt='2021') 
    LTO=AccessRecords.objects.filter(date__month__lt='5')
    LTO=AccessRecords.objects.filter(date__month__lte='6')

    d={'LTO':LTO}
    return render(request,'display_access.html',d)