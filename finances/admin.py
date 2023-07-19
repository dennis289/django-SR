from django.contrib import admin

# Register your models here.
from.models import feeBalance
from.models import feePayments

admin.site.register(feeBalance)
admin.site.register(feePayments)