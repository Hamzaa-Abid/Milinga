# Generated by Django 3.0.2 on 2020-02-18 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0009_auto_20200214_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workingtime',
            old_name='user',
            new_name='teacher',
        ),
    ]
