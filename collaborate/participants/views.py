from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Participant, ProjectParticipant

class ParticipantListView(ListView):
    model = Participant
    template_name = "participants/participant_list.html"
    context_object_name = "participants"

class ParticipantDetailView(DetailView):
    model = Participant
    template_name = "participants/participant_detail.html"
    context_object_name = "participant"

class ProjectParticipantListView(ListView):
    model = ProjectParticipant
    template_name = "participants/projectparticipant_list.html"
    context_object_name = "project_participants"

class ProjectParticipantDetailView(DetailView):
    model = ProjectParticipant
    template_name = "participants/projectparticipant_detail.html"
    context_object_name = "project_participant"

def create_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()  # Creates a Participant instance
            return redirect('participants_list')  # Redirect after successful creation
    else:
        form = ParticipantForm()

    return render(request, 'create_participant.html', {'form': form})
