from django.core.paginator import Paginator
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import Reserve_Student
from .models import Teacher, Reserve, Time_Table
from django.contrib.auth.models import User
from datetime import date

from django.core.exceptions import *


def index(request):
	teacher = Teacher.objects.order_by('id')
	reserve = Reserve.objects.all()
	context = {'teacher' : teacher, 'reserve': reserve}
	return render(request, 'qna.html', context)


def detail(request, teacher_id):
	today = date.today()
	teacher = Teacher.objects.get(id=teacher_id)
	reserve = Reserve.objects.order_by('id')
	context = {'teacher' : teacher, 'reserve' : reserve, 'today' : today}
	return render(request, 'qna_detail.html', context)


@login_required(login_url='common:login')
def reserve(request, reserve_id):
		reserve = Reserve.objects.get(id=reserve_id)
		reserve.student_name = request.user
		reserve.save()
		return render(request, 'reserve_complete.html')
	

@login_required(login_url='common:login')
def reserve_delete(request, reserve_id):
	reserve = Reserve.objects.get(id=reserve_id)
	reserve.student_name = None
	reserve.save()
	return render(request, 'reserve_delete.html')