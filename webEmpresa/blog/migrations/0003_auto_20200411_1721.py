# Generated by Django 3.0.4 on 2020-04-11 17:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200408_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 17, 21, 0, 53811, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
