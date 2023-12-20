# Generated by Django 4.2.7 on 2023-12-20 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('primary', '0002_rename_name_employees_first_name_employees_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='superuser',
            name='password',
            field=models.CharField(default='default_password', max_length=200),
        ),
        migrations.AlterField(
            model_name='superuser',
            name='employee_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]