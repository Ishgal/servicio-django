from django import forms
from .models import task
from django import forms
class Taskform(forms.ModelForm):
    class Meta:
        model = task
        fields=['Equipo','Cantidad','Serial','Bien_Nacional','Nota','Fecha_entrega']
        widgets = {
            
            'Fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
            'Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Coloque el nombre del equipo aqui.'}),
            'Cantidad': forms.TextInput(attrs={'class':'form-control','placeholder': 'Coloque la cantidad aqui.'}),
            'Serial': forms.TextInput(attrs={'class':'form-control','placeholder': 'Coloque el serial aqui.'}),
            'Bien_Nacional': forms.TextInput(attrs={'class':'form-control','placeholder': 'Coloque el bien nacional aqui.'}),
            'Nota': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Coloque una nota que pueda ayudar a llevar el control de este inventario. '}),
            
            
        }