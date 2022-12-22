# Generated by Django 4.1.4 on 2022-12-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0002_delete_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('className', models.CharField(max_length=1000, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Standard',
                'verbose_name_plural': 'Standards',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectName', models.CharField(max_length=1000, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
    ]