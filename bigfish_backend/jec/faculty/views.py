from re import A
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty
# Create your views here.
def FacultyData(request):
    fdata=Faculty.objects.all()
    # fname=[a.name for a in fdata]
    # f_name_str="\n".join(fname)
    # return HttpResponse("Our faculty names are:\n>>"+f_name_str)
    Department_query = request.GET.get('Department')
    Teacher_query = request.GET.get('Teacher')
    print(Department_query)
    if Department_query != '' and Department_query is not None:
        fdata = fdata.filter(department__icontains=Department_query)
    if Teacher_query != '' and Teacher_query is not None:
        fdata = fdata.filter(name__icontains=Teacher_query)
    context={'queryset':fdata}
    return render(request,'faculty/facultydata.html',context)
