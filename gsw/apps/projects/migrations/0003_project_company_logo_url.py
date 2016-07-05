# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_project_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='company_logo_url',
            field=models.TextField(default=datetime.datetime(2016, 7, 4, 12, 45, 59, 697068, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
