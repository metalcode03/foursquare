from django.urls import path
from  .views import index, upload
urlpatterns = [
    path('', index, name='index'),
    path('uploaded/<name>/', upload, name='upload'),
]
