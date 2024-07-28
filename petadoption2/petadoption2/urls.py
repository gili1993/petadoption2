from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petadoption2app.urls')),  # Include the app's URLs
]
