from django.shortcuts import render
from .serializers import emp_infoserializer
from rest_framework.decorators import api_view  
from .models import emp_info
from rest_framework.response import Response 

# Create your views here.

@api_view(['GET'])

def user_list(requset):
	if requset.method == 'GET':
		data = emp_info.objects.all()
		data1 = emp_infoserializer()
		return Response(data1)
		
