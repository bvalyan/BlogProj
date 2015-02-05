# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=datetime.datetime(2015, 2, 5, 18, 24, 9, 422576), max_length=60),
            preserve_default=False,
        ),
    ]
