# Generated by Django 4.2.5 on 2023-10-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest_projects', '0004_item_background_image_item_project_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='item_id',
            field=models.IntegerField(),
        ),
    ]
