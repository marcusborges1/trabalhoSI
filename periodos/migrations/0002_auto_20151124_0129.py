# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('periodos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='ano',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='semestre',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
