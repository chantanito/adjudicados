# Create your views here.
from django.shortcuts import render_to_response
from solicitudes.models import Solicitudes
from forms import SolicitudesForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.mail import send_mail

def home(request):
    entradas = Solicitudes.objects.all()[:10]
    return render_to_response('index.html', {'solicitudes' : entradas})

def thanks(request):
    return render_to_response('thanks.html')

def crear(request):
    if request.POST:
        form = SolicitudesForm(request.POST)
        if form.is_valid():
            nombre = form.clean_data['nombre']
            observaciones = form.clean_data['observaciones']
            email = form.clean_data.get('email', 'noreply@gmvvmerida.com')
            send_mail('Se ha cargado una solicitud de vivienda', 'Alguien ha cargado una vivienda', 'admin@gmvvmerida.com')
            return HttpResponseRedirect('/crear/gracias/')
    else:
        form = SolicitudesForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('crear_solicitud.html', args)

#def crear(request):
#    if request.POST:
#        form = SolicitudesForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/')
#    else:
#        form = SolicitudesForm()
#
#    args = {}
#    args.update(csrf(request))
#
#    args['form'] = form
#
#    return render_to_response('crear_solicitud.html', args)

def todas(request):
    solicitudes = Solicitudes.objects.all()[:10]
    return render_to_response('index.html', {'todas': solicitudes})

def consultar(request, solicitud_id=1):
    consulta = Solicitudes.objects.get(id=solicitud_id)
    return render_to_response('index.html', {'consultar': consulta})
