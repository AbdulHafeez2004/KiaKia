# Generated by Django 4.0 on 2023-01-10 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KiaKiaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
