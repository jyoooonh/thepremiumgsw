from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name



class Time_Table(models.Model):
	time = models.CharField(max_length=10)

	def __str__(self):
		return self.time


class Reserve(models.Model):
	time = models.ForeignKey(Time_Table, on_delete=models.CASCADE, null=True)
	teacher_name = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
	student_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	