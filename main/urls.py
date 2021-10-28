from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'main'

urlpatterns = [
    path('', hello, name='hello'),
    path('student_list', student_list, name='student_list'),
    path('teacher_list', teacher_list, name='teacher_list'),
    path('groups_list', groups_list, name='groups_list'),
    path('schedule', scheduleview, name='schedule'),
    path('schedule_detail', scheduleview, name='schedule_detail'),
    path('schedule/email', EmailFormView, name='email'),
]