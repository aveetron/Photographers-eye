from django.shortcuts import render
from .models import Personal_information,Image


# Create your views here.
def home(request):
    personal = Personal_information.objects.get(id=1)
    return render(request, 'index.html',{'personal': personal})


def work(request):
    img = Image.objects.all()
    return render(request, 'work.html', {'img': img})