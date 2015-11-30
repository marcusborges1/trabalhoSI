from django.http import HttpResponse

from django.shortcuts import render


from .models import Periodo


def index(request):
    #now = "15:50"
    #html = "<html><title>Periodos UnB</title><body>It is now <strong>%s</strong>.</body></html>" % now
    #template = loader.get_template('periodosunb/index.html')
    

    #string = ""
    #for p in Periodo.objects.all():
    #	string += "Periodo:%d/%d\n" % (p.ano, p.semestre)

    return render(request, 'periodosunb/index.html')

def detail(request, periodo_id): # Teste
    return HttpResponse("You're looking at question %s." % periodo_id)

def results(request, periodo_id):
	response = "Teste Teste id = %s."
	return HttpResponse(response % periodo_id)