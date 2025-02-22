# Generated by Django 3.0 on 2019-12-15 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('videoUrl', models.URLField(help_text='Video URL')),
                ('acceptsBitcoins', models.BooleanField(default=False)),
                ('acceptsFiat', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherTeaches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='subjects.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teaches', to='teachers.Teacher')),
            ],
        ),
    ]
