# Generated by Django 3.0.2 on 2020-02-18 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendarapp', '0010_auto_20200218_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingtime',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working_times', to=settings.AUTH_USER_MODEL),
        ),
    ]
