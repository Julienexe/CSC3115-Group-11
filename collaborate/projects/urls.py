from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # Project URLs
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
    
    # Outcome URLs
    path('outcomes/', views.OutcomeListView.as_view(), name='outcome-list'),
    path('outcomes/create/', views.OutcomeCreateView.as_view(), name='outcome-create'),
    path('outcomes/<int:pk>/', views.OutcomeDetailView.as_view(), name='outcome-detail'),
    path('outcomes/<int:pk>/update/', views.OutcomeUpdateView.as_view(), name='outcome-update'),
    path('outcomes/<int:pk>/delete/', views.OutcomeDeleteView.as_view(), name='outcome-delete'),
]
