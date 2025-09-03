from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # Project URLs
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('<uuid:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('<uuid:pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('<uuid:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
    
    # Outcome URLs
    path('outcomes/', views.OutcomeListView.as_view(), name='outcome-list'),
    path('outcomes/create/', views.OutcomeCreateView.as_view(), name='outcome-create'),
    path('outcomes/<uuid:pk>/', views.OutcomeDetailView.as_view(), name='outcome-detail'),
    path('outcomes/<uuid:pk>/update/', views.OutcomeUpdateView.as_view(), name='outcome-update'),
    path('outcomes/<uuid:pk>/delete/', views.OutcomeDeleteView.as_view(), name='outcome-delete'),
]
