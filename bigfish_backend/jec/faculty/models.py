from email.policy import default
from django.db import models

# Create your models here.
class Faculty(models.Model):
    department= models.CharField(max_length=400)
    designation=models.CharField(
        max_length=20,
        choices=[('Professor','Professor'),('Asst Professor','Asst Professor'),('Associate professor','Associate professor')]
    )
    name = models.CharField(max_length=200)
    dob=models.DateField()
    l=models.CharField(
        max_length=2,
        choices=[('PG','undergraduate'),('PG','post graduate')],default='UG')
    doa=models.DateField()
    exp=models.IntegerField(default=0)
    regular=models.BooleanField(default=True)
    def __str__(self):
        return self.name
# d={}
# import pandas as pd
# facultydf = pd.read_csv(r'E:\bigfish_backend\jec\faculty\faculty.csv')

# print(facultydf)
# for (row,rowseries) in facultydf.iterrows():
#     print(row)
#     d[row]={}
#     # p=Faculty()
#     # li=[p.department,p.designation,p.name,p.dob,p.l,p.doa,p.exp]
#     #li=['p.department','p.designation','p.name','p.dob','p.l','p.doa','p.exp']
#     i=0
#     for val in rowseries:
#         print(val)
#         # li[i]=val
#         d[row][i]=str(val)
#         i+=1


# i=0
# for a in range(73):
#     p=Faculty()
#     p.department=str(d[a][0])
#     p.designation=str(d[a][1])
#     p.name=str(d[a][2])
#     p.dob=str(d[a][3])
#     p.l=str(d[a][4])
#     p.doa=str(d[a][5])
#     p.save()

