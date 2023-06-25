# Generated by Django 4.2.2 on 2023-06-06 16:51

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('photo', models.ImageField(default='', null=True, upload_to='photos')),
                ('PhonNumber', models.CharField(max_length=16, null=True, verbose_name='رقم الموبايل')),
                ('emp_company', models.IntegerField(null=True)),
                ('is_busy', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='اسم المستخدم')),
                ('password', models.CharField(max_length=128, verbose_name='كلمة المرور')),
            ],
            options={
                'verbose_name': ' المرور',
                'verbose_name_plural': ' يالمرور',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TypeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameType', models.CharField(blank=True, max_length=15, null=True)),
                ('desc', models.CharField(max_length=50)),
                ('photo', models.ImageField(null=True, upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('address', models.CharField(blank=True, max_length=40)),
                ('is_active', models.BooleanField(default=True)),
                ('emp_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customuser')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='TypeUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.typeaccount', verbose_name='نوع الحساب'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_name', models.CharField(blank=True, default='', max_length=10)),
                ('address_city', models.CharField(blank=True, default='', max_length=10)),
                ('address_street', models.CharField(blank=True, default='', max_length=10)),
                ('address_latitude', models.CharField(blank=True, default='', max_length=10)),
                ('address_longitude', models.CharField(blank=True, default='', max_length=10)),
                ('address_coustem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customuser')),
            ],
        ),
    ]