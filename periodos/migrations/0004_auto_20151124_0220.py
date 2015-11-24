# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('periodos', '0003_auto_20151124_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='admissao_mudanca_curso',
            field=models.IntegerField(verbose_name=b'admiss\xc3\xb5es por Mudan\xc3\xa7a de Curso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='admissao_pas',
            field=models.IntegerField(verbose_name=b'admiss\xc3\xb5es por PAS'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='admissao_transf_obrig',
            field=models.IntegerField(verbose_name=b'admiss\xc3\xb5es por Transf. Obrigat\xc3\xb3ria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='admissao_vest',
            field=models.IntegerField(verbose_name=b'admiss\xc3\xb5es por Vestibular'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='aprovados_disciplinas',
            field=models.IntegerField(verbose_name=b'aprovados em Disciplinas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='cumpriram_monitoria',
            field=models.IntegerField(verbose_name=b'cumpriram Monitoria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='desligamento_abandono',
            field=models.IntegerField(verbose_name=b'desligamento por Abandono'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='desligamento_jubilamento',
            field=models.IntegerField(verbose_name=b'desligamento por Jubilamento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='desligamento_rendimento',
            field=models.IntegerField(verbose_name=b'desligamento por Rendimento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='desligamento_voluntario',
            field=models.IntegerField(verbose_name=b'desligamento Volunt\xc3\xa1rio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='falecimento',
            field=models.IntegerField(verbose_name=b'falecidos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='matricula_aluno_esp',
            field=models.IntegerField(verbose_name=b'matriculas de Alunos Especiais'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='matriculados_disciplinas',
            field=models.IntegerField(verbose_name=b'matr\xc3\xadculas em Disciplinas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='reprovados_disciplinas',
            field=models.IntegerField(verbose_name=b'reprovados em Discip\xc4\xbainas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='tracamento_justificado',
            field=models.IntegerField(verbose_name=b'tracamentos Justificados'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='trancamento',
            field=models.IntegerField(verbose_name=b'trancamentos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='trancamento_geral_matr',
            field=models.IntegerField(verbose_name=b'trancamentos Gerais de Matr\xc3\xadculas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='transferencia_outras_ies',
            field=models.IntegerField(verbose_name=b'transfer\xc3\xaancia para outras IES'),
            preserve_default=True,
        ),
    ]
