# Generated by Django 4.1.4 on 2023-02-19 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('joiningDate', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='default.png', upload_to='userimage/')),
                ('aboutme', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('mobile', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('Staff', 'Staff'), ('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'CustomUser',
                'verbose_name_plural': 'CustomUsers',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('salary', models.IntegerField(default=0)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_session_active', models.BooleanField(default=False)),
                ('is_fees_clear', models.BooleanField(default=False)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.domain')),
                ('standard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.standard')),
                ('subdomain', models.ManyToManyField(blank=True, to='base.subdomain')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authentication.employee')),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.domain')),
                ('subdomain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.subdomain')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
            bases=('authentication.employee',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authentication.employee')),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.department')),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staffs',
            },
            bases=('authentication.employee',),
        ),
    ]
