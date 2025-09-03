# apps/capstone/serializers.py
from rest_framework import serializers
from .models import Program, Project, Outcome

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ["id", "name", "description", "national_alignment", "focus_areas", "phases", "created_at", "updated_at"]


class ProjectSerializer(serializers.ModelSerializer):
    program_name = serializers.ReadOnlyField(source="program.name")

    class Meta:
        model = Project
        fields = [
            "id", "program", "program_name", "title", "nature_of_project", "description",
            "innovation_focus", "prototype_stage", "testing_requirements", "commercialization_plan",
            "created_at", "updated_at"
        ]


class OutcomeSerializer(serializers.ModelSerializer):
    project_title = serializers.ReadOnlyField(source="project.title")

    class Meta:
        model = Outcome
        fields = [
            "id", "project", "project_title", "title", "description", "artifact_file",
            "artifact_link", "outcome_type", "quality_certification", "commercialization_status",
            "created_at", "updated_at"
        ]

    def validate(self, attrs):
        file_ = attrs.get("artifact_file")
        link_ = attrs.get("artifact_link")
        if not file_ and not link_:
            raise serializers.ValidationError(
                "Provide at least one of: artifact_file upload or artifact_link URL."
            )
        return attrs
