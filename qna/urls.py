from django.urls import path

from . import views

app_name = 'qna'

urlpatterns = [
	path('', views.index, name='index'),
	path('reserve_detail/<int:teacher_id>/', views.detail, name="detail"),
	path('reserve_complete/<int:reserve_id>', views.reserve, name='reserve_complete'),
	path('reserve_delete/<int:reserve_id>', views.reserve_delete, name='reserve_delete'),
  path('comment_create/<int:reserve_id>', views.comment_create, name='comment_create'),
  path('comment_modify/<int:reserve_id>', views.comment_modify, name='comment_modify')
]