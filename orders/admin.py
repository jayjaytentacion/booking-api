from django.contrib import admin
from .models import Transit,Booking

# Register your models here.
admin.site.register(Booking)
admin.site.register(Transit)