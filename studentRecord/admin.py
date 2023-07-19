from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import student
from .models import hostel
from .models import hostel_allocation
from .models import registration

admin.site.register(student)
admin.site.register(hostel)
admin.site.register(hostel_allocation)
admin.site.register(registration)
