# Generated by Django 3.0.5 on 2021-05-13 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20210513_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_book_call',
            name='advisor_id',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='all_book_call',
            name='advisor_image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='all_book_call',
            name='booking_id',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='all_book_call',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='all_book_call',
            name='advisor_name',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
