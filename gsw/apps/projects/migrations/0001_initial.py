# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('company_logo', models.ImageField(upload_to='')),
                ('text', models.TextField()),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
