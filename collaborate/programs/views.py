from django.shortcuts import render
from django.http import FileResponse, Http404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Program
from .serializers import ProgramSerializer

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

        data = request.data.copy()
        data["program"] = program.id
        serializer = ProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


