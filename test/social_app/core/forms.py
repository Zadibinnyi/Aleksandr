from django import forms
from .models import Download

class UploadDocumentForm(forms.Form):
    file = forms.FileField()  
    class Meta:
        model = Download
        fields = ('data', 'name', 'size', 'file')