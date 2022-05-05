from django.urls import path
from . import views

urlpatterns = [
    path('getcontactus/',views.getcontactus),
    path('getaboutus/',views.getaboutus),
    path('getservice_sub_category/',views.getservice_sub_category),
    path('getservice_category/',views.getservice_category),
    path('gettestimonials/',views.gettestimonials),
    path('getfeedback/',views.getfeedback)
]
