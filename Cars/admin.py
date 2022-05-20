from django.contrib import admin
from .models import NewCar,UsedCar,RentCar,BrandLogos
# Register your models here.
admin.site.register(NewCar)
admin.site.register(UsedCar)
admin.site.register(RentCar)
admin.site.register(BrandLogos)
admin.site.site_header='Car Showroom Admin Page'
admin.site.site_title='Admin Page'

"""class CarAdmin(admin.ModelAdmin):
    list_display=['ad_title','type','brand','price','active']
    list_display_links=['ad_title']
    list_editable=['price','active']
    search_fields=['ad_title']
    list_filter=['type','brand','price','transmission_type','model_year']"""