from django.urls import path
from  . import views as v
urlpatterns = [
    path('', v.index, name='index'),
    path('uploaded/<name>/', v.upload, name='upload'),
    path('export_csv/', v.export_csv, name='export-csv'),
    path('export_excel/', v.export_excel, name='export-excel'),
]