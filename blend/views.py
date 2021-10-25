from django.shortcuts import render, redirect
from .forms import UploadForms
from .models import UploadAndBlendImg

# Create your views here.
def index(request):
    forms = UploadForms(request.POST, request.FILES)
    if forms.is_valid():
        forms.save()
        upload = UploadAndBlendImg.objects.get(name=forms.cleaned_data.get("name"))
        return redirect(f'/uploaded/{upload.name}/')
    forms = UploadForms()
    context = {
        "form": forms
    }
    return render(request, 'index.html', context)

def upload(request, name):
    uploaded = UploadAndBlendImg.objects.get(name=name)
    context = {
        "upload": uploaded
    }
    return render(request, 'test.html', context)
    
