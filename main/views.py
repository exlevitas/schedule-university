import datetime

from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def hello(request):
    return render(request, 'hello.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students':students})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers':teachers})


def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', {'groups':groups})


def scheduleview(request):
    today = datetime.date.today()
    start_week = today - datetime.timedelta(days=today.weekday())
    end_week = start_week + datetime.timedelta(days=7)
    schedules = Schedule.objects.select_related().all()
    schedule_mon = schedules.filter(day='MO')
    schedule_tue = schedules.filter(day='TU')
    schedule_wed = schedules.filter(day='WE')
    schedule_thu = schedules.filter(day='TH')
    schedule_fri = schedules.filter(day='FR')
    schedule_sat = schedules.filter(day='SA')
    schedule_sun = schedules.filter(day='SU')

    context = {
        'start_week': start_week,
        'end_week': end_week,
        'schedule_mon': schedule_mon,
        'schedule_tue': schedule_tue,
        'schedule_wed': schedule_wed,
        'schedule_thu': schedule_thu,
        'schedule_fri': schedule_fri,
        'schedule_sat': schedule_sat,
        'schedule_sun': schedule_sun,
        'schedules':schedules,
    }

    return render(request, 'schedule.html', context)


def EmailFormView(request):
    form = GetEmail(request.POST)
    abc = {'form':form}
    if request.method == 'POST' and form.is_valid():
            data = form.cleaned_data
            form.save()
    return render(request, 'email_form.html', abc)