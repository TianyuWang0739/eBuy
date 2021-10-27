
from django.shortcuts import render


# Create your views here.
import templates


def index(request):
    return render(request,'index.html')
