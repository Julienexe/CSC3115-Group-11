from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
  
    path('outcomes/', views.OutcomeListView.as_view(), name='outcome-list'),
    path('outcomes/<int:pk>/', views.OutcomeDetailView.as_view(), name='outcome-detail'),
 
]
