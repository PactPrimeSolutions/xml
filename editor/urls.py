# editor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),  # The default view when visiting /upload/
    path('download/', views.download_xml, name='download_xml'),  # The view for downloading XML
]
