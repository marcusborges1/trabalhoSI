# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Periodo

class PeriodoAdmin(admin.ModelAdmin):
	fieldsets = [
		('Período',			{'fields': ['ano','semestre']}),
		('Alunos',			{'fields': ['total_alunos_regulares','total_alunos_ativos']}),
		('Admissões',		{'fields': ['admissao_vest','admissao_pas','admissao_transf_obrig','admissao_mudanca_curso','matricula_aluno_esp']}),
		('Desligamentos',	{'fields': ['formados','transferencia_outras_ies','desligamento_voluntario','desligamento_rendimento','desligamento_abandono','desligamento_jubilamento','falecimento']}),
		('Disciplinas',		{'fields': ['matriculas_disciplinas','aprovacao_disciplinas','reprovacao_disciplinas']}),
		('Trancamentos',	{'fields': ['trancamento','tracamento_justificado','trancamento_geral_matr']}),
		('Extras',			{'fields': ['cumpriram_monitoria']})
	]

admin.site.register(Periodo,PeriodoAdmin)