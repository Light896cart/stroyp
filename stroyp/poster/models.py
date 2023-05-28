from django.db import models
from django.urls import reverse


class Order(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    phoneNumber = models.CharField(max_length=12,verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True,verbose_name='Время изменения')
    paid = models.BooleanField(default=False,verbose_name='Выполнен')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class Work(models.Model):
    name = models.CharField(max_length=70,verbose_name='Что делали')
    address = models.CharField(max_length=70,verbose_name='Адрес')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    square = models.CharField(max_length=70,verbose_name='Площадь',null=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo1 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo2 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo3 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo4 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo5 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo6 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo7 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo8 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo9 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo10 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo11 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo12 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo13 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo14 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo15 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name='Фото')
    class Meta:
        ordering = ('-name',)
        verbose_name = 'Готовые продукты'
        verbose_name_plural = 'Готовые продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})
