# Generated by Django 3.0.3 on 2020-03-27 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit',
            old_name='dateBooked',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='credit',
            old_name='student',
            new_name='payed',
        ),
        migrations.RenameField(
            model_name='credit',
            old_name='teacher',
            new_name='received',
        ),
    ]
