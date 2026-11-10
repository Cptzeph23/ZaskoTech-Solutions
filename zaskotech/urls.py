from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', RedirectView.as_view(pattern_name='index', permanent=True)),
    path('', include('zaskoapp.urls')),
]
