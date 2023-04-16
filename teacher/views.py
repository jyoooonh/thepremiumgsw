from django.shortcuts import render

from qna.models import Teacher, Reserve
from .models import Consulting
from .forms import ConsultingForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator


def index(request):
    return HttpResponse("안녕하세요. teacher 페이지 입니다.")


@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def main(request):
    consulting = Consulting.objects.order_by('-id')
    teacher = Teacher.objects.order_by('id')
        
    page = request.GET.get('page', '1')
    paginator = Paginator(consulting, 15)
    page_obj = paginator.get_page(page)

    context = {'teacher': teacher, 'consulting': page_obj}
    return render(request, 'teacher/teacher_page.html', context)


@login_required(login_url='common:login')
def consulting_detail(request, consulting_id):
	consulting = Consulting.objects.get(id=consulting_id)
	context = {'consulting': consulting}
	return render(request, 'teacher/consulting_detail.html', context)


@login_required(login_url='common:login')
def consulting_create(request):
    if request.method == 'POST':
        form = ConsultingForm(request.POST)
        if form.is_valid():
            consulting = form.save(commit=False)
            consulting.teacher_name = request.user
            consulting_type = form.cleaned_data.get('consulting_type')
            if consulting_type == 'other':
                other_consulting_type = form.cleaned_data.get('other_consulting_type')
                consulting.consulting_type = other_consulting_type
            else:
                consulting.consulting_type = consulting_type
            consulting.save()
            return redirect('teacher:main')
    else:
        form = ConsultingForm()
    context = {'form': form}
    return render(request, 'teacher/consulting_form.html', context)



@login_required(login_url='common:login')
def reserve_detail(request, teacher_id):
	page = request.GET.get('page', '1')	# 페이지
	teacher = Teacher.objects.get(id=teacher_id)
	reserve_filter = Reserve.objects.filter(teacher_id=teacher_id, student_name__isnull=False).order_by('-id')
	paginator = Paginator(reserve_filter, 10)	# 페이지당 10개씩 보여주기
	page_obj = paginator.get_page(page)

	context = {'teacher' : teacher, 'reserve' : page_obj }
	return render(request, 'teacher/teacher_detail.html', context)