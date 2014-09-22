from django.conf.urls import patterns, url

from adjudicados import views

urlpatterns = patterns('',
    #ejemplo: /adjudicados/
    url(r'^$', views.index, name='index'),
    #ejemplo: /adjudicados/3/
    url(r'^(?P<adjudicado_id>\d+)/$', views.detail, name='detail'),
    #ejemplo: /adjudicados/3/resultados
    url(r'^(?P<adjudicado_id>\d+)/results/$', views.results, name='results'),
    #ejemplo: /adjudicados/3/votos/
    url(r'^(?P<adjudicado_id>\d+)/vote/$', views.vote, name='vote')
)