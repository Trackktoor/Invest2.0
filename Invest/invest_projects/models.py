"""
    Модели для Item
"""
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


def save_image(instance, filename):
    try:
        return '/'.join([settings.MEDIA_ROOT,'itemsimgs', str(instance.item_id), filename])
    except:
        return '/'.join([settings.MEDIA_ROOT,'itemsimgs', str(instance.id), filename])



class Category(models.Model):
    """
        Категория для объявления
    """
    title = models.CharField(max_length=220)
    parent_category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)


class Item(models.Model):
    """
        Проект от пользователя
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255, blank=True, null=True)
    required_investment = models.IntegerField(blank=True, null=True)
    profit_per_month = models.CharField(max_length=255, blank=True, null=True)
    profit_parametr = models.CharField(max_length=100,default='Месяц')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    images = models.ManyToManyField(
        'ItemImage', related_name='images_for_item')
    background_image = models.ImageField(upload_to=save_image, blank=True, null=True, max_length=500)
    project_avatar = models.ImageField(upload_to=save_image, blank=True, null=True,max_length=500)
    contacts = models.CharField(max_length=500, blank=True, null=True)
    count_view = models.IntegerField(default=0)
    count_get_contacts = models.IntegerField(default=0)
    count_add_favorite = models.ManyToManyField(
        User, related_name='favorite_items', blank=True)
    status = models.CharField(max_length=100, default='Проверяется')
    paid_verification = models.BooleanField(default=False)
    author_job_title = models.CharField(max_length=200, default='Директор')

    def __str__(self):
        return str(self.title)

    def get_count_add_favorite(self):
        return len(self.count_add_favorite.all())
    

class ItemImage(models.Model):
    """
        Модель для картинок объявлений
    """
    item_id = models.IntegerField(blank=True, null=True)
    image = models.ImageField(
        upload_to=save_image, blank=True, null=True, max_length=500)
