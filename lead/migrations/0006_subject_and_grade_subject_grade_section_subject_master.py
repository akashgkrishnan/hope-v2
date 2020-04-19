# Generated by Django 2.2 on 2020-04-19 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0005_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='subject_grade_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lead.grade_section_master')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lead.subject_master')),
            ],
        ),
        migrations.CreateModel(
            name='subject_and_grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lead.grade_master')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lead.subject_master')),
            ],
        ),
    ]
