from django.urls import path

from . import views

app_name = 'teacher'

urlpatterns = [
		path('', views.index),
    path('main/', views.main, name='main'),
    path('consulting_detail/<int:consulting_id>', views.consulting_detail, name="consulting_detail"),
    path('consulting_create/', views.consulting_create, name="consulting_create"),
    path('<int:teacher_id>/', views.reserve_detail, name="reserve_detail")
]