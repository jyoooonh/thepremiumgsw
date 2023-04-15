from django.urls import path

from . import views

app_name = 'teacher'

urlpatterns = [
		path('', views.index),
    path('main/', views.main, name='main'),
    path('<int:teacher_id>/', views.detail, name="detail")
]
