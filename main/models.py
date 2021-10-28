from django.db import models

# Create your models here.


class Teacher(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    middlename = models.CharField(max_length=50, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.surname


class Group(models.Model):
    group_name = models.CharField(max_length=20)
    group_count = models.IntegerField()

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.group_name


class Student(models.Model):
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    middlename = models.CharField(max_length=50, verbose_name='Отчество')

    class Meta:
        verbose_name='Студент'
        verbose_name_plural='Студенты'

    def __str__(self):
        return self.surname



class Schedule(models.Model):
    DAY_CHOICES = (
		('MON', 'Понедельник'),
		('TUE', 'Вторник'),
		('WED', 'Среда'),
		('THU', 'Четверг'),
		('FRI', 'Пятница'),
		('SAT', 'Суббота'),
		('SUN', 'Воскресенье'),
	)

    day = models.CharField(max_length=3, choices=DAY_CHOICES, verbose_name='День недели')
    time = models.TimeField(verbose_name='Время занятия')
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель', on_delete=models.CASCADE)

    class Meta:
        ordering = ['day']
        verbose_name = ('Расписание занятий')
        verbose_name_plural = ('Расписание занятий')

    def __str__(self):
        return self.day

class Email(models.Model):
    author = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.email