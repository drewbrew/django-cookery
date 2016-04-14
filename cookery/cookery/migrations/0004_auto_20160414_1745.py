# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0003_auto_20160413_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Tags', to='cookery.RecipeTag'),
        ),
    ]