# Generated by Django 4.1.4 on 2022-12-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_staff_staffbio_alter_teacher_teacherbio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staffBio',
            field=models.TextField(default='Bio'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staffImage',
            field=models.ImageField(default='default.png', upload_to='staffimage/'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staffMobileNumber',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentBio',
            field=models.TextField(default='Bio'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentImage',
            field=models.ImageField(default='default.png', upload_to='studentimage/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentMarks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentMobileNumber',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentRemarks',
            field=models.TextField(default='Remarks'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacherBio',
            field=models.TextField(default='Bio'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacherImage',
            field=models.ImageField(default='default.png', upload_to='teacherimage/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacherMobileNumber',
            field=models.CharField(default='', max_length=100),
        ),
    ]