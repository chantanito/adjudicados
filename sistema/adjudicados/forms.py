from django import forms

OPCIONES_TERRENO = (
    ('S', 'Si'),
    ('N', 'No'),
)

class Terreno(forms.Form):
    posesion = forms.ChoiceField(choices=OPCIONES_TERRENO)
    tenencia = forms.ChoiceField(choices=OPCIONES_TERRENO)
    condiciones = forms.ChoiceField(choices=OPCIONES_TERRENO)

def __unicode__(self):
	return self.posesion + self.tenencia + self.condiciones