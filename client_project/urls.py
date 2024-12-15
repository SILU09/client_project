# client_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Home page view (optional)
def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the API URLs
    path('', home),  # Add this line to handle the root URL
]
