from django.urls import path
from . import views

app_name = 'participants'

urlpatterns = [
    path('', views.ParticipantListView.as_view(), name='participant-list'),
    path('<uuid:pk>/', views.ParticipantDetailView.as_view(), name='participant-detail'),
    path('create/', views.create_participant, name='participant-create'),
]
