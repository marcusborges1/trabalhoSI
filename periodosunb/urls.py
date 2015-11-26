from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /periodosunb
    url(r'^$', views.index, name='index'),
    # /periodosunb/5
    url(r'^(?P<periodo_id>[0-9]+)/$', views.detail, name='detail'),
    # /periodosunb/5/results
    url(r'^(?P<periodo_id>[0-9]+)/results/$', views.results, name='results'),
]