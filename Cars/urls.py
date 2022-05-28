from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('newcars',views.newcars,name='newcars'),
    path('usedcars',views.usedcars,name='usedcars'),
    path('sell',views.sell,name='sell'),
    path('new/<int:id>',views.newcar,name='newcar'),
    path('used/<int:id>',views.usedcar,name='usedcar'),
    path('rent/<int:id>',views.rentcar,name='rentcar'),
    path('rentcars',views.rentcars,name='rentcars'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('extra',views.footer,name='footerLinks'),
]
