from django.shortcuts import render, get_object_or_404
from adjudicados.models import Adjudicado, DatosSociales
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    #return HttpResponse("Hola hola, traje pollito")
    ultimos_adjudicados = Adjudicado.objects.order_by('-fecha_de_publicacion')[:3]
    context = {'ultimos_adjudicados': ultimos_adjudicados}
    return render(request, 'adjudicados/index.html', context)

def detail(request, adjudicado_id):
    adjudicados = get_object_or_404(Adjudicado, pk=adjudicado_id)
    return render(request, 'adjudicados/detail.html', {'adjudicados': adjudicados})

def results(request, adjudicado_id):
    return HttpResponse("Est&aacute;s viendo los resultados de los adjudicados %s." % adjudicado_id)

def vote(request, adjudicado_id):
    return HttpResponse("Est&aacute;s viendo los votos del adjudicado %s." % adjudicado_id)