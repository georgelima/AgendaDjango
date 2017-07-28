
from django import forms
from models import ItemAgenda

#
# FormItemAgenda
#
class FormItemAgenda(forms.ModelForm):
    class Meta:
        model  = ItemAgenda
        fields = ('data','hora','titulo','descricao')

