# -*- coding: utf-8 -*-
from django.http import HttpResponse 
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from graphos.sources.model import SimpleDataSource
from graphos.renderers import gchart

from periodosunb.models import Periodo

queryset = Periodo.objects.all()

def index(request):
    template = loader.get_template('graficos/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def graficoalunos(request):
    chart_data = []
    chart_data.append(['Período', 'Alunos Regulares', 'Alunos Ativos'])
    for d in queryset:
        chart_data.append(['{0}/{1}'.format(d.semestre, d.ano),
            d.total_alunos_regulares,
            d.total_alunos_ativos])

    grafico = gchart.ColumnChart(SimpleDataSource(data=chart_data), options={'title': "Alunos"})

    return render_to_response('graficos/graficoalunos.html', {'grafico': grafico})

def graficoadmissoes(request):
    chart_data = []
    chart_data.append(['Período', 'Vestibular', 'PAS', 'Transf.', 'Mudança de Curso', 'Matrícula de Aluno Especial'])
    for d in queryset:
        chart_data.append(['{0}/{1}'.format(d.semestre, d.ano),
            d.admissao_vest,
            d.admissao_pas,
            d.admissao_transf_obrig,
            d.admissao_mudanca_curso,
            d.matricula_aluno_esp])

    grafico = gchart.ColumnChart(SimpleDataSource(data=chart_data), options={'title': "Admissões"})

    return render_to_response('graficos/graficoadmissoes.html', {'grafico': grafico})

def graficodesligamentos(request):
    chart_data = []
    chart_data.append(['Período', 'Formados', 'Transf.', 'Voluntário', 'Rendimento', 'Abandono', 'Jubilamento', 'Falecimento'])
    for d in queryset:
        chart_data.append(['{0}/{1}'.format(d.semestre, d.ano),
            d.formados,
            d.transferencia_outras_ies,
            d.desligamento_voluntario,
            d.desligamento_rendimento,
            d.desligamento_abandono,
            d.desligamento_jubilamento,
            d.falecimento])

    grafico = gchart.ColumnChart(SimpleDataSource(data=chart_data), options={'title': "Desligamentos"})

    return render_to_response('graficos/graficodesligamentos.html', {'grafico': grafico})

def graficodisciplinas(request):
    chart_data = []
    chart_data.append(['Período', 'Matrículas', 'Aprovações', 'Reprovações'])
    for d in queryset:
        chart_data.append(['{0}/{1}'.format(d.semestre, d.ano),
            d.matriculas_disciplinas,
            d.aprovacao_disciplinas,
            d.reprovacao_disciplinas])

    grafico = gchart.ColumnChart(SimpleDataSource(data=chart_data), options={'title': "Disciplinas"})

    return render_to_response('graficos/graficodisciplinas.html', {'grafico': grafico})

def graficotrancamentos(request):
    chart_data = []
    chart_data.append(['Período', 'Trancamentos', 'Trancamento Justificado', 'Trancamento Geral de Matrícula'])
    for d in queryset:
        chart_data.append(['{0}/{1}'.format(d.semestre, d.ano),
            d.trancamento,
            d.tracamento_justificado,
            d.trancamento_geral_matr])

    grafico = gchart.ColumnChart(SimpleDataSource(data=chart_data), options={'title': "Trancamentos"})

    return render_to_response('graficos/graficotrancamentos.html', {'grafico': grafico})
