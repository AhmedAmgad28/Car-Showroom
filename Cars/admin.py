from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(NewCar)
admin.site.register(UsedCar)
admin.site.register(RentCar)
admin.site.register(BrandL)
admin.site.site_header='Car Showroom Admin Page'
admin.site.site_title='Admin Page'
