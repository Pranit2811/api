from django.urls import path
from . import views
urlpatterns = [
    path('show',views.getitem,name='home'),
    path('add',views.additem,name='home'),
    path('api/<int:delay_value>',views.delaytimecounter,name='counter'),

]
