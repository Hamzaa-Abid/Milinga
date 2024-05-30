# Generated by Django 3.0.3 on 2020-07-06 19:38

from django.db import migrations
import imagekit.models.fields
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200617_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilePic',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=profiles.models.generate_profilePic_filename),
        ),
    ]
