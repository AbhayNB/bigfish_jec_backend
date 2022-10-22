from django.contrib import admin
from .models import Faculty
class FacultyAdmin(admin.ModelAdmin):
    list_display=['name','department','designation','dob','doa','exp','regular']
# Register your models here.
admin.site.register(Faculty,FacultyAdmin)