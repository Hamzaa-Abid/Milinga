# Generated by Django 3.0 on 2019-12-23 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_auto_20191223_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calevent',
            old_name='userConfirmed',
            new_name='studentConfirmed',
        ),
    ]
