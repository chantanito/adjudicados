from django.conf.urls import patterns, include, url
from solicitudes import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistema.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^adjudicados/', include('adjudicados.urls', namespace="adjudicados")),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^reportes-admin/', include(views.reporte)),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^report_builder/', include('report_builder.urls'))
)