# Generated by Django 4.2.5 on 2023-10-04 19:41

import account.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_last_acivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.save_image),
        ),
        migrations.AlterField(
            model_name='profile',
            name='inn',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.save_image),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_acivity',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 4, 22, 41, 14, 35825)),
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
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=account.models.save_image)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='images',
            field=models.ManyToManyField(related_name='images_for_profile', to='account.profileimage'),
        ),
    ]
