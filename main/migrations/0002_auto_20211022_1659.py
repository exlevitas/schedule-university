# Generated by Django 3.2.8 on 2021-10-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'Расписание занятий', 'verbose_name_plural': 'Расписание занятий'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
        migrations.AlterField(
            model_name='group',
            name='group_count',
            field=models.IntegerField(),
        ),
    ]