from django import forms
from .models import Cliente


class RegistroForm(forms.ModelForm):

    class Meta: 
        model = Cliente
        fields=[
                'nombre',
                'direccion',
                'comuna',
                'correo',
        ]

        labels={
                'nombre':'Nombre Cliente',
                'direccion':'direccion',
                'comuna':'comuna',
                'correo':'correo',

        }


