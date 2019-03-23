from django.db import models

# Create your models here.

class emp_info(models.Model):
	emp_name = models.CharField(max_length=20)
	emp_deprt = models.CharField(max_length=20)
	emp_porject = models.CharField(max_length=50)
	emp_mobile = models.CharField(max_length=10)
	def __str__(self):
		return self.emp_name	