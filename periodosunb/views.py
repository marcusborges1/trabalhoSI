from django.http import HttpResponse
from django.template import RequestContext, loader


from .models import Periodo


def index(request):
    template = loader.get_template('periodosunb/index.html')
    return HttpResponse(template)

def detail(request, periodo_id): # Teste
    return HttpResponse("You're looking at question %s." % periodo_id)

def results(request, periodo_id):
	response = "Teste Teste id = %s."
	return HttpResponse(response % periodo_id)