from django import forms

class ZapatillaForm(forms.Form):
    modelo= forms.CharField(max_length=50, required=True)
    talle= forms.IntegerField(required=True)
    
class NikeForm(forms.Form):
    modelo= forms.CharField(max_length=50, required=True)
    talle= forms.IntegerField()
    
class PumaForm(forms.Form):
    modelo= forms.CharField(max_length=50, required=True)
    talle= forms.IntegerField()
    
class RemerasForm(forms.Form):
    color= forms.CharField(max_length=50, required=True)
    talle= forms.IntegerField()

    