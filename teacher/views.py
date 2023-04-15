from django.shortcuts import render

from qna.models import Teacher, Reserve
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.core.paginator import Paginator

def index(request):
    return HttpResponse("안녕하세요. teacher 페이지 입니다.")

def main(request):
	teacher = Teacher.objects.order_by('id')
	reserve = Reserve.objects.all()
	context = {'teacher' : teacher, 'reserve': reserve}
	return render(request, 'teacher/teacher_page.html', context)


@login_required(login_url='common:login')
def detail(request, teacher_id):
	page = request.GET.get('page', '1')	# 페이지
	teacher = Teacher.objects.get(id=teacher_id)
	reserve_filter = Reserve.objects.filter(teacher_id=teacher_id, student_name__isnull=False).order_by('-id')
	paginator = Paginator(reserve_filter, 10)	# 페이지당 10개씩 보여주기
	page_obj = paginator.get_page(page)

	context = {'teacher' : teacher, 'reserve' : page_obj }
	return render(request, 'teacher/teacher_detail.html', context)

@login_required(login_url='common:login')
def consulting_detail(request, teacher_id):
	page = request.GET.get('page', '1')
	
