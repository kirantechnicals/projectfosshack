# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('title', models.CharField(default='Not available', max_length=300, primary_key=True, serialize=False)),
                ('text', models.TextField(default='Not available')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('title', models.CharField(default='Not available', max_length=300, primary_key=True, serialize=False)),
                ('description', models.TextField(default='Not available')),
                ('url', models.URLField(default='Not available')),
                ('urlToImage', models.URLField(default='Not available')),
                ('publishedAt', models.CharField(blank=True, default='Not available', max_length=100, null=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('positive', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('negative', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('neutral', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('label', models.CharField(default='Not available', max_length=300)),
                ('anger', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('calm', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('fear', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('happy', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('like', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('shame', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('sure', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('surprise', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
            ],
        ),
    ]
