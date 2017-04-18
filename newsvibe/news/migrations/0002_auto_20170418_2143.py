# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default='Not available'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publishedAt',
            field=models.CharField(default='Not available', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default='Not available', max_length=300),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.URLField(default='Not available'),
        ),
        migrations.AlterField(
            model_name='news',
            name='urlToImage',
            field=models.URLField(default='Not available'),
        ),
    ]
