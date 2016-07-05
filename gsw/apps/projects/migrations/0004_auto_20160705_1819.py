# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_company_logo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='company_logo_alt',
            field=models.TextField(default=datetime.datetime(2016, 7, 5, 16, 19, 4, 380071, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='company_url',
            field=models.TextField(default=datetime.datetime(2016, 7, 5, 16, 19, 14, 190133, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
