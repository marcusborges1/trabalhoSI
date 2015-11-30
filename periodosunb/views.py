from django.http import HttpResponse

from django.shortcuts import render


from .models import Periodo


def index(request):
    periodos_list = Periodo.objects.order_by("ano")
    context = {'periodos_list': periodos_list}
    return render(request, 'periodosunb/index.html', context)

def detail(request, periodo_id): # Teste
    return HttpResponse("You're looking at question %s." % periodo_id)

def results(request, periodo_id):
	response = "Teste Teste id = %s."
	return HttpResponse(response % periodo_id)