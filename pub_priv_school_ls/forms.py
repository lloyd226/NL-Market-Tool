from django import forms

class InputData(forms.Form):
    input_latitude = forms.DecimalField(max_digits=10, decimal_places=7)
    input_longitude = forms.DecimalField(max_digits=10, decimal_places=7)
    radius = forms.DecimalField(max_digits=4, decimal_places=2)