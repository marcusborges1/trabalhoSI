from django.db import models


class Periodo(models.Model):

	# 2-tuplas para o widget da view
	ANOS_PERMITIDOS = (
		(2009, '2009'),
		(2010, '2010'),
		(2011, '2011'),
		(2012, '2012'),
		(2013, '2013'),
		(2014, '2014'),
		(2015, '2015'),
	)

	SEMESTRES_PERMITIDOS = (
		(1, '1'),
		(2, '2'),
	)

	# Periodo
	ano = models.IntegerField(choices=ANOS_PERMITIDOS)
	semestre = models.IntegerField(choices=SEMESTRES_PERMITIDOS)

	# Admissoes
	admissao_vest = models.IntegerField()
	admissao_pas = models.IntegerField()
	admissao_transf_obrig = models.IntegerField()
	admissao_mudanca_curso = models.IntegerField()
	matricula_aluno_esp = models.IntegerField()
	
	# Desligamentos
	formados = models.IntegerField()
	transferencia_outras_ies = models.IntegerField()
	desligamento_voluntario = models.IntegerField()
	desligamento_rendimento = models.IntegerField()
	desligamento_abandono = models.IntegerField()
	desligamento_jubilamento = models.IntegerField()
	falecimento = models.IntegerField()

	# Disciplinas
	matriculados_disciplinas = models.IntegerField()
	aprovados_disciplinas = models.IntegerField()
	reprovados_disciplinas = models.IntegerField()
	
	# Trancamentos
	trancamento = models.IntegerField()
	tracamento_justificado = models.IntegerField()
	trancamento_geral_matr = models.IntegerField()
	
	# Extras
	cumpriram_monitoria = models.IntegerField()
	
