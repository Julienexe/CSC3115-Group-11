from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Participant
from .forms import ParticipantForm

class ParticipantListView(ListView):
    model = Participant
    template_name = "participants/participant_list.html"
    context_object_name = "participants"

class ParticipantDetailView(DetailView):
    model = Participant
    template_name = "participants/participant_detail.html"
    context_object_name = "participant"
    
def create_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()  # Creates a Participant instance
            return redirect('participants:participant-list')  # Redirect after successful creation
    else:
        form = ParticipantForm()

    return render(request, 'participants/create_participant.html', {'form': form})
