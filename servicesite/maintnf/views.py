from django.shortcuts import render
from requests import Response
from .models import contact_us
from .serializers import ContactSerializers
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def getcontactus(request):
    obj = contact_us.objects.all()
    objser = ContactSerializers(obj,many=True)
    objser.save()
    return Response(objser.data)