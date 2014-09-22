from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^todas/$', 'solicitudes.views.todas'),
    url(r'^consultar/(?P<solicitud_id>\d+)/$', 'solicitudes.views.consultar'),
)