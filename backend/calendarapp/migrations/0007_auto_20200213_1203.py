# Generated by Django 3.0.2 on 2020-02-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0006_auto_20200211_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calevent',
            name='studentConfirmed',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='calevent',
            name='teacherConfirmed',
            field=models.BooleanField(),
        ),
    ]
