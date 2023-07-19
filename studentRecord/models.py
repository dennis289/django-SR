from django.db import models
# Create your models here.
from django.db import models
class registration(models.Model):
    id=models.AutoField
    admin_no= models.CharField(max_length=4)

class student(models.Model):
    Full_name= models.CharField(max_length=30)
    reg_no= models.CharField(max_length=10,default='')
    email=models.EmailField(max_length=40)
    contact=models.IntegerField(default=15)
    registration=models.ForeignKey(registration,on_delete=models.CASCADE,default=10)
    
class hostel(models.Model):
    hostel_name= models.CharField(max_length=20)
    Room_no=models.FloatField
    Occupants=models.IntegerField(default=0)
 

class hostel_allocation(models.Model):
    hostel_allocation=models.BooleanField(auto_created=False)
    dateAllocated=models.DateField(auto_now=True)