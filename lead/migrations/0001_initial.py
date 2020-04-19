# Generated by Django 2.2 on 2020-04-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='busMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_reg_number', models.CharField(max_length=12)),
                ('status', models.CharField(choices=[('A', 'Active'), ('X', 'Inactive')], default='A', max_length=1)),
                ('Owner_Mobile', models.CharField(max_length=12)),
                ('owner_name', models.CharField(max_length=12)),
                ('bus_Route_start_to_end', models.CharField(max_length=65)),
            ],
        ),
    ]
