# Generated by Django 4.1.4 on 2022-12-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_teacher_student'),
        ('base', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='Admitted_Student', to='user.student'),
        ),
    ]
