# Generated by Django 3.0.5 on 2021-05-13 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210513_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_model',
            name='advisor_image',
            field=models.ImageField(blank=True, default='', upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='can_book_call',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 5, 13, 9, 33, 51, 132249)),
        ),
    ]
