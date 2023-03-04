from django.urls import path

from . import views

app_name = 'qna'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:teacher_id>/', views.detail, name="detail"),
	path('reserve/', views.reserve, name='reserve'),
]