# Generated by Django 4.2.6 on 2024-02-25 07:24

import account.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_profile_avatar_alter_profile_inn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=account.models.save_image),
        ),
        migrations.AlterField(
            model_name='profile',
            name='inn',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.save_image),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_acivity',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 25, 7, 24, 46, 144012)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ogrn',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.save_image),
        ),
        migrations.AlterField(
            model_name='profile',
            name='passport',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.save_image),
        ),
        migrations.AlterField(
            model_name='profile',
            name='snils',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.save_image),
        ),
    ]