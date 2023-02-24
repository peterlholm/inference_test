from django import forms

class ApiForm(forms.Form):
    api_key = forms.CharField(max_length=100, required=True)
    index = forms.CharField(max_length=100, required=True)
    color = forms.ImageField(required=True)
    # fringe = forms.FileField(required=True)

class ApiTestForm(forms.Form):
    api_key = forms.CharField(max_length=100, required=False)
    index = forms.CharField(max_length=100, required=False)
    # color = forms.FileField(required=False)
    # fringe = forms.FileField(required=False)
