# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('periodos', '0002_auto_20151124_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='semestre',
            field=models.IntegerField(choices=[(1, b'1'), (2, b'2')]),
            preserve_default=True,
        ),
    ]
