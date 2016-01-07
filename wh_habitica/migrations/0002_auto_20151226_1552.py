# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitica',
            name='api_token',
            field=models.CharField(blank=True, max_length=255, verbose_name='API Token'),
        ),
        migrations.AlterField(
            model_name='habitica',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='habitica',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='habitica',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='User ID'),
        ),
    ]