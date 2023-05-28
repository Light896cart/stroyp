# Generated by Django 4.1.3 on 2023-02-26 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeriy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo1', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo2', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo3', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo4', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo5', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo6', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo7', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo8', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo9', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo10', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo11', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo12', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo13', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo14', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('photo15', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='poster.galeriy', verbose_name='Выберите подкатегорию'),
        ),
    ]
