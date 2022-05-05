from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def getcontactus(request):
    obj = contact_us.objects.all()
    print(obj)
    objser = ContactSerializers(obj,many=True)
    return Response(objser.data)

@api_view(['GET'])
def getaboutus(request):
    obj = about_us.objects.all()
    print(obj)
    objser = AboutSerializers(obj,many=True)
    return Response(objser.data)

@api_view(['GET'])
def getservice_sub_category(request):
    obj = service_sub_category.objects.all()
    print(obj)
    objser = Service_sub_categorySerializers(obj,many=True)
    return Response(objser.data)

@api_view(['GET'])
def getservice_category(request):
    obj = service_category.objects.all()
    print(obj)
    objser = Service_categorySerializers(obj,many=True)
    return Response(objser.data)

@api_view(['GET'])
def gettestimonials(request):
    obj = testimonials.objects.all()
    print(obj)
    objser = TestimonialsSerializers(obj,many=True)
    return Response(objser.data)

@api_view(['GET'])
def getfeedback(request):
    obj = feedback.objects.all()
    print(obj)
    objser = FeedbackSerializers(obj,many=True)
    return Response(objser.data)