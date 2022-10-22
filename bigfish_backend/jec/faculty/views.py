from re import A
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty
# Create your views here.
def FacultyData(request):
    fdata=Faculty.objects.all()
    fname=[a.name for a in fdata]
    f_name_str="\n".join(fname)
    return HttpResponse("Our faculty names are:\n>>"+f_name_str)