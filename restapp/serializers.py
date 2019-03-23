from rest_framework import serializers 
from .models import emp_info

class emp_infoserializer(serializers.ModelSerializer):
	class Metta:
		model = emp_info
		fields = '__all__'