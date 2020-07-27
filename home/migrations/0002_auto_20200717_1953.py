# Generated by Django 3.0.7 on 2020-07-17 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homedb',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterField(
            model_name='homedb',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت'),
        ),
        migrations.AlterField(
            model_name='homedb',
            name='document',
            field=models.TextField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='homedb',
            name='photo',
            field=models.ImageField(upload_to='images', verbose_name='تصویره مقاله'),
        ),
        migrations.AlterField(
            model_name='homedb',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='homedb',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله'),
        ),
        migrations.AlterField(
            model_name='homedb',
            name='status',
            field=models.CharField(choices=[('D', 'پیش نویس'), ('P', 'منتشر شده')], max_length=1, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='homedb',
            name='tittle',
            field=models.CharField(max_length=100, verbose_name='عنوان مقاله'),
        ),
        migrations.AlterField(
            model_name='homedb',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی'),
        ),
    ]
