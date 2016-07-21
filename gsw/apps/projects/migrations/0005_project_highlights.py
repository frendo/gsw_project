# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20160705_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='highlights',
            field=models.TextField(default=datetime.datetime(2016, 7, 20, 9, 18, 2, 405562, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
