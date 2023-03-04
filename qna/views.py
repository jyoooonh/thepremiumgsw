from django.core.paginator import Paginator
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

import logging

from .forms import Reserve_Student
from .models import Teacher, Reserve

logger = logging.getLogger('qna')


def index(request):
	3 / 0		# 강제로 오류 발생
	teacher = Teacher.objects.order_by('id')
	context = {'teacher' : teacher}
	return render(request, 'qna.html', context)


def detail(request, teacher_id):
	teacher = Teacher.objects.get(id=teacher_id)
	#time = Reservation.objects.values('time')
	reserve = Reserve.objects.filter('time')
	context = {'teacher' : teacher, 'reserve' : reserve}
	return render(request, 'qna_detail.html', context)



@login_required(login_url='common:login')
def reserve(request):
	# 폼 파트로 넘어가서 views.py 작성
	if request.method == 'POST':
		form = Reserve_Student(request.POST)
		if form.is_valid():
			student = form.save(commit=False)
			Reserve.student_name = request.user
			student.save()
			form = Reserve_Student()
			return render(request, 'reserve_complete.html', {'form': form})
	else:
		form = Reserve_Student()
	#return render(request, 'reserve_complete.html', {'form': form})
	return redirect('qna:index')