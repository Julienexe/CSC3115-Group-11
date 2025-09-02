from django.urls import path
from . import views

app_name = 'program'

urlpatterns = [
    path('', views.ProgramListView.as_view(), name='program-list'),
    path('<int:pk>/', views.ProgramDetailView.as_view(), name='program-detail'),
    
]
