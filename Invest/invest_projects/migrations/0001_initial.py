# Generated by Django 4.2.5 on 2023-09-13 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import invest_projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invest_projects.category')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=invest_projects.models.save_image)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('required_investment', models.IntegerField(blank=True, null=True)),
                ('profit_per_month', models.CharField(blank=True, max_length=255, null=True)),
                ('contacts', models.CharField(blank=True, max_length=500, null=True)),
                ('count_view', models.IntegerField(default=0)),
                ('count_get_contacts', models.IntegerField(default=0)),
                ('status', models.CharField(default='Проверяется', max_length=100)),
                ('category', models.ManyToManyField(to='invest_projects.category')),
                ('count_add_favorite', models.ManyToManyField(related_name='favorite_items', to=settings.AUTH_USER_MODEL)),
                ('images', models.ManyToManyField(related_name='images_for_item', to='invest_projects.itemimage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
