# Generated by Django 5.0.6 on 2024-07-21 13:49

import app8.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=14, unique=True)),
                ('course_name', models.CharField(max_length=70)),
                ('course_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_usn', models.CharField(max_length=10, unique=True)),
                ('student_name', models.CharField(max_length=80)),
                ('student_sem', models.IntegerField(validators=[app8.models.valid_sem])),
                ('student_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('enrolment', models.ManyToManyField(to='app8.course')),
            ],
        ),
    ]
