# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/<int:id>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/<int:id>/', views.ProjectDetailView.as_view(), name='project_detail'),
]
