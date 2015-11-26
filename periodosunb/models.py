# -*- coding: utf-8 -*-

from django.db import models


class Periodo(models.Model):

	# 2-tuplas para o widget da view
	#ANOS_PERMITIDOS = (
	#	(2009, '2009'),
	#	(2010, '2010'),
	#	(2011, '2011'),
	#	(2012, '2012'),
	#	(2013, '2013'),
	#	(2014, '2014'),
	#	(2015, '2015'),
	#)

	SEMESTRES_PERMITIDOS = (
		(1, '1'),
		(2, '2'),
	)

	# Periodo
	ano = models.IntegerField()
	semestre = models.IntegerField(choices=SEMESTRES_PERMITIDOS)
    
	# Alunos
	total_alunos_regulares = models.IntegerField()
	total_alunos_ativos = models.IntegerField()

	# Admissoes
	admissao_vest = models.IntegerField("admissões por Vestibular")
	admissao_pas = models.IntegerField("admissões por PAS")
	admissao_transf_obrig = models.IntegerField("admissões por Transf. Obrigatória")
	admissao_mudanca_curso = models.IntegerField("admissões por Mudança de Curso")
	matricula_aluno_esp = models.IntegerField("matriculas de Alunos Especiais")
	
	# Desligamentos
	formados = models.IntegerField()
	transferencia_outras_ies = models.IntegerField("transferência para outras IES")
	desligamento_voluntario = models.IntegerField("desligamento Voluntário")
	desligamento_rendimento = models.IntegerField("desligamento por Rendimento")
	desligamento_abandono = models.IntegerField("desligamento por Abandono")
	desligamento_jubilamento = models.IntegerField("desligamento por Jubilamento")
	falecimento = models.IntegerField("falecidos")

	# Disciplinas
	matriculas_disciplinas = models.IntegerField("matrículas em Disciplinas")
	aprovacao_disciplinas = models.IntegerField("aprovação em Disciplinas")
	reprovacao_disciplinas = models.IntegerField("reprovação em Discipĺinas")
	
	# Trancamentos
	trancamento = models.IntegerField("trancamentos")
	tracamento_justificado = models.IntegerField("tracamentos Justificados")
	trancamento_geral_matr = models.IntegerField("trancamentos Gerais de Matrículas")
	
	# Extras
	cumpriram_monitoria = models.IntegerField("cumpriram Monitoria")
	
	# Metodos
	def __unicode__(self):
		periodo = str(self.ano)+"/"+str(self.semestre)
		return periodo