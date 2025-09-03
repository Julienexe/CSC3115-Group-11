from django.urls import path
from . import views

app_name = 'program'

urlpatterns = [
    path('', views.ProgramListView.as_view(), name='program-list'),
    path('create/', views.ProgramCreateView.as_view(), name='program-create'),
    path('<int:pk>/', views.ProgramDetailView.as_view(), name='program-detail'),
    path('<int:pk>/update/', views.ProgramUpdateView.as_view(), name='program-update'),
    path('<int:pk>/delete/', views.ProgramDeleteView.as_view(), name='program-delete'),
]
