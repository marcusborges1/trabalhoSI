from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^graficoalunos/$', views.graficoalunos, name='graficoalunos'),
    url(r'^graficoadmissoes/$', views.graficoadmissoes, name='graficoadmissoes'),
    url(r'^graficodesligamentos/$', views.graficodesligamentos, name='graficodesligamentos'),
    url(r'^graficodisciplinas/$', views.graficodisciplinas, name='graficodisciplinas'),
    url(r'^graficotrancamentos/$', views.graficotrancamentos, name='graficotrancamentos'),
]
