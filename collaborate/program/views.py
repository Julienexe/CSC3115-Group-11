# apps/capstone/views.py
from django.http import FileResponse, Http404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Program, Project, Outcome
from .serializers import ProgramSerializer, ProjectSerializer, OutcomeSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    """
    Implements 'Organize Work Under a Program':
    - list/retrieve/create/update/destroy Programs
    - list/create Projects under a Program (via /programs/{id}/projects/) :contentReference[oaicite:4]{index=4}
    """
    queryset = Program.objects.all().order_by("-created_at")
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["get", "post"], url_path="projects")
    def projects(self, request, pk=None):
        program = self.get_object()

        if request.method.lower() == "get":
            qs = program.projects.all().order_by("-created_at")
            page = self.paginate_queryset(qs)
            serializer = ProjectSerializer(page, many=True) if page is not None else ProjectSerializer(qs, many=True)
            return self.get_paginated_response(serializer.data) if page is not None else Response(serializer.data)

        # POST -> create a project under this program
        data = request.data.copy()
        data["program"] = program.id
        serializer = ProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    - CRUD for Projects (global list)
    - List/Create Outcomes under a Project (via /projects/{id}/outcomes/) :contentReference[oaicite:5]{index=5}
    """
    queryset = Project.objects.select_related("program").all().order_by("-created_at")
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["get", "post"], url_path="outcomes")
    def outcomes(self, request, pk=None):
        project = self.get_object()

        if request.method.lower() == "get":
            qs = project.outcomes.all().order_by("-created_at")
            page = self.paginate_queryset(qs)
            serializer = OutcomeSerializer(page, many=True) if page is not None else OutcomeSerializer(qs, many=True)
            return self.get_paginated_response(serializer.data) if page is not None else Response(serializer.data)

        # POST -> create outcome under this project
        data = request.data.copy()
        data["project"] = project.id
        serializer = OutcomeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OutcomeViewSet(viewsets.ModelViewSet):
    """
    Implements 'Capture Project Outcomes':
    - list/retrieve/create/update/delete Outcomes
    - Download linked artifact_file via /outcomes/{id}/download/ :contentReference[oaicite:6]{index=6}
    """
    queryset = Outcome.objects.select_related("project", "project__program").all().order_by("-created_at")
    serializer_class = OutcomeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["get"], url_path="download")
    def download(self, request, pk=None):
        outcome = self.get_object()
        if not outcome.artifact_file:
            raise Http404("This outcome has no uploaded file.")
        return FileResponse(outcome.artifact_file.open("rb"), as_attachment=True, filename=outcome.artifact_file.name.split("/")[-1])

