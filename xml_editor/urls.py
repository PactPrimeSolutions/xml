# xml_editor/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='upload/', permanent=False)),  # Redirect root URL to /upload/
    path('upload/', include('editor.urls')),  # Include URLs from editor app
]
