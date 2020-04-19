# Generated by Django 2.2 on 2020-04-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=40)),
                ('book_author', models.CharField(max_length=40)),
                ('genre', models.CharField(choices=[('ACTION', 'ACTION'), ('ROMANCE', 'ROMANCE'), ('THRILLER', 'THRILLER'), ('SUSPENSE', 'SUSPENSE'), ('COMEDY', 'COMEDY'), ('ACADMEDIC', 'ACADEMIC'), ('GENERAL', 'GENERAL'), ('STORYBOOK', 'STORYBOOK')], max_length=15)),
                ('number_of_books', models.PositiveIntegerField()),
                ('book_number', models.CharField(max_length=15)),
            ],
        ),
    ]
