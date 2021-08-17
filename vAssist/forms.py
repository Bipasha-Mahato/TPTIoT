from django import forms
from .models import vQuery

class vQueryForm(forms.ModelForm):
    
    class Meta:
        model = vQuery
        fields = ('complainant_name','subject','complaint')