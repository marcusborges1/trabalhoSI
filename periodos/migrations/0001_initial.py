# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ano', models.IntegerField(choices=[(2009, b'2009'), (2010, b'2010'), (2011, b'2011'), (2012, b'2012'), (2013, b'2013'), (2014, b'2014'), (2015, b'2015')])),
                ('semestre', models.IntegerField(choices=[(1, b'1'), (2, b'2')])),
                ('admissao_vest', models.IntegerField()),
                ('admissao_pas', models.IntegerField()),
                ('admissao_transf_obrig', models.IntegerField()),
                ('admissao_mudanca_curso', models.IntegerField()),
                ('matricula_aluno_esp', models.IntegerField()),
                ('formados', models.IntegerField()),
                ('transferencia_outras_ies', models.IntegerField()),
                ('desligamento_voluntario', models.IntegerField()),
                ('desligamento_rendimento', models.IntegerField()),
                ('desligamento_abandono', models.IntegerField()),
                ('desligamento_jubilamento', models.IntegerField()),
                ('falecimento', models.IntegerField()),
                ('matriculados_disciplinas', models.IntegerField()),
                ('aprovados_disciplinas', models.IntegerField()),
                ('reprovados_disciplinas', models.IntegerField()),
                ('trancamento', models.IntegerField()),
                ('tracamento_justificado', models.IntegerField()),
                ('trancamento_geral_matr', models.IntegerField()),
                ('cumpriram_monitoria', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
