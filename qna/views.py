from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Teacher, Reserve
from django.contrib.auth.models import User
from datetime import date
import datetime

from django.core.exceptions import *


def index(request):
	teacher = Teacher.objects.order_by('id')
	reserve = Reserve.objects.all()
	context = {'teacher' : teacher, 'reserve': reserve}
	return render(request, 'qna.html', context)


@login_required(login_url='common:login')
def detail(request, teacher_id):
	today = date.today()
	teacher = Teacher.objects.get(id=teacher_id)
	reserve = Reserve.objects.order_by('id')
	context = {'teacher' : teacher, 'reserve' : reserve, 'today' : today}
	return render(request, 'qna_detail.html', context)


@login_required(login_url='common:login')
def reserve(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    today = datetime.datetime.today().date()
    existing_reservation = Reserve.objects.filter(date=today, teacher_id=reserve.teacher_id, student_name=request.user).exists()
    if not existing_reservation:
        reserve.student_name = request.user
        reserve.save()
        return render(request, 'reserve_complete.html')
    else:
        messages.warning(request, '이미 예약하였습니다.')
        return redirect('qna:detail', teacher_id=reserve.teacher_id.id)
	

@login_required(login_url='common:login')
def reserve_delete(request, reserve_id):
	reserve = Reserve.objects.get(id=reserve_id)
	reserve.student_name = None
	reserve.save()
	return render(request, 'reserve_delete.html')


@login_required(login_url='common:login')
def comment_create(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reserve.comment_subject = form.cleaned_data['comment_subject']
            reserve.comment_content = form.cleaned_data['comment_content']
            reserve.save()
            teacher_id = reserve.teacher_id.id
            return redirect('qna:detail', teacher_id=teacher_id)
    else:
        form = CommentForm(instance=reserve)
    return render(request, 'comment_form.html', {'form': form})


@login_required(login_url="common:login")
def comment_modify(request, reserve_id):
    reserve = get_object_or_404(Reserve, id=reserve_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=reserve)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.reserve = reserve
            comment.save()
            teacher_id = reserve.teacher_id.id
            return redirect('qna:detail', teacher_id=teacher_id)
    else:
        form = CommentForm(instance=reserve)
    return render(request, 'comment_form.html', {'form': form})
