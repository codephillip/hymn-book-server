# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-31 07:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catetory',
            new_name='Category',
        ),
    ]
