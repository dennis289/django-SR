from django.db import models
from studentRecord.models import registration, student
# Create your models here.
class feeBalance(models.Model):
    registration=models.ForeignKey(registration, on_delete=models.CASCADE)
    student =models.ForeignKey(student ,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10 ,decimal_places=3)

class feePayments(models.Model):
    registration=models.ForeignKey(registration, on_delete=models.CASCADE)
    student =models.ForeignKey(student  ,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10 ,decimal_places=3)






