# Generated by Django 2.2 on 2020-08-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestant', '0004_auto_20200819_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.FileField(blank=True, upload_to='profile_images/'),
        ),
    ]
