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
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField(choices=[(1, b'1'), (2, b'2')])),
                ('admissao_vest', models.IntegerField(verbose_name=b'admiss\xc3\xb5es por Vestibular')),
                ('admissao_pas', models.IntegerField(verbose_name=b'admiss\xc3\xb5es por PAS')),
                ('admissao_transf_obrig', models.IntegerField(verbose_name=b'admiss\xc3\xb5es por Transf. Obrigat\xc3\xb3ria')),
                ('admissao_mudanca_curso', models.IntegerField(verbose_name=b'admiss\xc3\xb5es por Mudan\xc3\xa7a de Curso')),
                ('matricula_aluno_esp', models.IntegerField(verbose_name=b'matriculas de Alunos Especiais')),
                ('formados', models.IntegerField()),
                ('transferencia_outras_ies', models.IntegerField(verbose_name=b'transfer\xc3\xaancia para outras IES')),
                ('desligamento_voluntario', models.IntegerField(verbose_name=b'desligamento Volunt\xc3\xa1rio')),
                ('desligamento_rendimento', models.IntegerField(verbose_name=b'desligamento por Rendimento')),
                ('desligamento_abandono', models.IntegerField(verbose_name=b'desligamento por Abandono')),
                ('desligamento_jubilamento', models.IntegerField(verbose_name=b'desligamento por Jubilamento')),
                ('falecimento', models.IntegerField(verbose_name=b'falecidos')),
                ('matriculas_disciplinas', models.IntegerField(verbose_name=b'matr\xc3\xadculas em Disciplinas')),
                ('aprovacao_disciplinas', models.IntegerField(verbose_name=b'aprova\xc3\xa7\xc3\xa3o em Disciplinas')),
                ('reprovacao_disciplinas', models.IntegerField(verbose_name=b'reprova\xc3\xa7\xc3\xa3o em Discip\xc4\xbainas')),
                ('trancamento', models.IntegerField(verbose_name=b'trancamentos')),
                ('tracamento_justificado', models.IntegerField(verbose_name=b'tracamentos Justificados')),
                ('trancamento_geral_matr', models.IntegerField(verbose_name=b'trancamentos Gerais de Matr\xc3\xadculas')),
                ('cumpriram_monitoria', models.IntegerField(verbose_name=b'cumpriram Monitoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
