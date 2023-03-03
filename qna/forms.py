from django import forms
from django.contrib.auth.models import User
from .models import Teacher

class Reserve_Student(forms.ModelForm):
	# Meta 클래스에는 사용할 모델과 모델의 속성을 적어야함
	class Meta:
		model = User
		fields = ['username']

class Reserve_Teacher(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ['name']