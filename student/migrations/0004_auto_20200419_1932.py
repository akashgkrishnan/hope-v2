# Generated by Django 2.2 on 2020-04-19 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_attendance_history_studentattendance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='studentAttendance',
            new_name='student_attendance',
        ),
    ]
