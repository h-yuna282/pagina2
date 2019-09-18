from django import forms
from .models import pago,detalle_pago

from django.forms.models import inlineformset_factory

from django.forms import SelectDateWidget

class pagoForm(forms.ModelForm):

    class Meta:
        model = pago
        fields = ['forma_de_pago','reserva']

    def __init__(self, *args, **kwargs):
        super(pagoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class detalle_pagoForm(forms.ModelForm):
        
    class Meta:
        model = detalle_pago
        fields = ['observaciones','pago','reserva']

    def __init__(self, *args, **kwargs):
        super(detalle_pagoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            

detalle_pagoFormSet = inlineformset_factory(pago, detalle_pago, form=detalle_pagoForm, extra=3)