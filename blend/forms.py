from django import forms
from .models import UploadAndBlendImg

class UploadForms(forms.ModelForm):
    class Meta:
        model = UploadAndBlendImg
        fields = (
            'name',
            'fileUpload',
        )
        