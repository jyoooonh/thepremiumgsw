from django.urls import path

from . import views

app_name = 'qna'

urlpatterns = [
	#path('', views.index, name='index'),
	path('<int:teacher_id>/', views.detail, name="detail"),
	path('reserve_complete/<int:reserve_id>', views.reserve, name='reserve_complete'),
	path('reserve_delete/<int:reserve_id>', views.reserve_delete, name='reserve_delete')
]