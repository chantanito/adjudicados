from django import forms
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms.formsets import formset_factory

SINO_CHOICES = (
	('S', 'Si'),
	('N', 'No'),
)

class SolicitudesForm(forms.Form):

	PROFESION_CHOICES = (
		('N', 'No Aplica'),
		('P', 'Primaria'),
		('B', 'Bachiller'),
		('S', 'Tecnico Superior'),
		('U', 'Universitaria')
		)

	nombre = forms.CharField(max_length=12, label="Nombre")
	snombre = forms.CharField(max_length=12, required=False, label="Segundo Nombre")
	apellido = forms.CharField(max_length=15, label="Apellido")
	sapellido = forms.CharField(max_length=15, required=False, label="Segundo Apellido")
	cedula = forms.CharField(max_length=8, required=True, label="Cedula")
	fecha_nacimiento = forms.DateTimeField(label="Fecha de Nacimiento", widget=SelectDateWidget, required=False)
	tel1 = forms.CharField(max_length=11, label="Telefono Celular")
	tel2 = forms.CharField(max_length=11, required=False, label="Telefono Fijo")
	cotizacion = forms.ChoiceField(choices=SINO_CHOICES, label="Cotiza FAOV", widget=forms.RadioSelect)
	profesion = forms.ChoiceField(choices=PROFESION_CHOICES)
	email = forms.EmailField(max_length=42, label="Correo Electronico")
	observaciones = forms.CharField(max_length=400, initial="No hay observaciones", widget=forms.Textarea)
	SERVICIOS_CHOICES = (
		('AP', 'Agua Potable'),
		('AS', 'Agua Servida'),
		('E', 'Electricidad'),
		('G', 'Gas'),
		('V', 'Vialidad'),
		('T', 'Telefonia'),
	)
	posesion = forms.ChoiceField(choices=SINO_CHOICES)
	servicios = forms.MultipleChoiceField(SERVICIOS_CHOICES)
	tenencia = forms.ChoiceField(choices=SINO_CHOICES)
	ESTADO_CHOICES = (
		('AM', 'Amazonas'),
		('AZ', 'Anzoategui'),
		('AP', 'Apure'),
		('AR', 'Aragua'),
		('BA', 'Barinas'),
		('BO', 'Bolivar'),
		('CA', 'Carabobo'),
		('CO', 'Cojedes'),
		('DA', 'Delta Amacuro'),
		('DC', 'Distrito Capital'),
		('FA', 'Falcon'),
		('GU', 'Guarico'),
		('LA', 'Lara'),
		('ME', 'Merida'),
		('MI', 'Miranda'),
		('MO', 'Monagas'),
		('NE', 'Nueva Esparta'),
		('PO', 'Portuguesa'),
		('SU', 'Sucre'),
		('TA', 'Tachira'),
		('TR', 'Trujillo'),
		('VA', 'Vargas'),
		('YA', 'Yaracuy'),
		('ZU', 'Zulia'),
		)
	estado = forms.ChoiceField(ESTADO_CHOICES)
	municipio = forms.CharField()
	parroquia = forms.CharField()
	sector = forms.CharField(max_length=150)
	calle = forms.CharField(max_length=20, label="Av./Calle")
	casa = forms.CharField(max_length=20, label="Edificio/Casa")
	ncasa = forms.CharField(max_length=4, label="N Casa/Apartamento")
