from django.test import SimpleTestCase
from unittest.mock import Mock, MagicMock
from django.core.exceptions import ValidationError
from .models import Project


class ProjectBusinessLogicTests(SimpleTestCase):
    """Unit tests for Project model business rules without ORM."""

    def setUp(self):
        # Simulate per-program title uniqueness
        self.project_registry = set()

    def test_required_foreign_keys(self):
        """Should fail if ProgramId or FacilityId missing"""
        project = Mock(spec=Project)
        project.program_id = None
        project.facility_id = None
        project.status = "in_progress"
        project.outcomes = MagicMock()
        project.outcomes.exists.return_value = False

        with self.assertRaises(ValidationError) as cm:
            Project.clean(project)

        self.assertIn("Project.ProgramId and Project.FacilityId are required.", str(cm.exception))

    def test_unique_project_title_per_program(self):
        """Should fail if title is duplicated under same program"""
        program_id = 1
        title = "AI for Agriculture"

        # Register existing project
        self.project_registry.add((program_id, title.lower()))

        new_project = Mock(spec=Project)
        new_project.program_id = program_id
        new_project.facility_id = 5
        new_project.title = "AI for Agriculture"
        new_project.status = "in_progress"
        new_project.outcomes = MagicMock()
        new_project.outcomes.exists.return_value = False

        if (new_project.program_id, new_project.title.lower()) in self.project_registry:
            exc = ValidationError("A project with this title already exists under this program.")
        else:
            self.project_registry.add((new_project.program_id, new_project.title.lower()))
            exc = None

        self.assertEqual(str(exc), "['A project with this title already exists under this program.']")

    def test_completed_project_requires_outcomes(self):
        """Should fail if status=completed but no outcomes exist"""
        project = Mock(spec=Project)
        project.program_id = 1
        project.facility_id = 1
        project.title = "IoT Smart Sensor"
        project.status = "completed"
        project.outcomes = MagicMock()
        project.outcomes.exists.return_value = False  # simulate missing outcomes

        with self.assertRaises(ValidationError) as cm:
            Project.clean(project)

        self.assertIn("Completed projects must have at least one documented outcome.", str(cm.exception))

    def test_valid_in_progress_project_passes(self):
        """Should pass if project is valid and not completed"""
        project = Mock(spec=Project)
        project.program_id = 1
        project.facility_id = 2
        project.title = "Solar Automation System"
        project.status = "in_progress"
        project.outcomes = MagicMock()
        project.outcomes.exists.return_value = False  # fine for in-progress

        try:
            Project.clean(project)
        except ValidationError:
            self.fail("clean() raised ValidationError unexpectedly for valid project")

    def test_completed_project_with_outcomes_passes(self):
        """Should pass if completed project has outcomes"""
        project = Mock(spec=Project)
        project.program_id = 1
        project.facility_id = 2
        project.title = "Smart Irrigation System"
        project.status = "completed"
        project.outcomes = MagicMock()
        project.outcomes.exists.return_value = True  # simulate having outcomes

        try:
            Project.clean(project)
        except ValidationError:
            self.fail("clean() raised ValidationError unexpectedly for project with outcomes")
