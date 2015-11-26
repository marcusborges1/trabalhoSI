# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('periodosunb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='total_alunos_ativos',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='periodo',
            name='total_alunos_regulares',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
    ]
