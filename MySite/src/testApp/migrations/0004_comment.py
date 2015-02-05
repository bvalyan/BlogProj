# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_auto_20150127_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('post', models.ForeignKey(to='testApp.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
