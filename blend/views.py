from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForms
from .models import UploadAndBlendImg
import datetime
import csv
import xlwt

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

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Desposition'] = 'attachment; filename=Expenses' + str(datetime.datetime.now()) + '.csv'
    
    writer = csv.writer(response)
    row = ["name", "file_upload", "file_genrated"]
    writer.writerow(row)
    
    uploads = UploadAndBlendImg.objects.all()
    
    for upload in uploads:
        writer.writerow([upload.name, upload.fileUpload, upload.bgUpload])
    
    return response

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Desposition'] = 'attachment; filename=Expenses' + str(datetime.datetime.now()) + '.xls'
    
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    column = ["name", "file_upload", "file_genrated"]
    
    for col_num in range(len(column)):
        ws.write(row_num, col_num, column[col_num], font_style)
        
    font_style = xlwt.XFStyle()
    
    rows = UploadAndBlendImg.objects.all().values_list(
        "name", "fileUpload", "bgUpload")
    
    for row in rows:
        row_num += 1
        
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
            
    wb.save(response)
    return response