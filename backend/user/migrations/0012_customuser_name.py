# Generated by Django 4.1.4 on 2022-12-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_staff_staffid_remove_student_studentid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]