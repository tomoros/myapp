# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-20 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kusyokyuu',
            old_name='question',
            new_name='question1',
        ),
        migrations.AddField(
            model_name='kusyokyuu',
            name='question2',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kusyokyuu',
            name='question3',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kusyokyuu',
            name='question4',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
