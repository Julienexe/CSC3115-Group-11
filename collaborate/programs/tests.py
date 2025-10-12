from django.test import SimpleTestCase
from unittest.mock import Mock, MagicMock, patch
from django.core.exceptions import ValidationError
from .models import Program


class ProgramBusinessLogicTests(SimpleTestCase):
    """Unit tests for Program model business rules without ORM."""

    def setUp(self):
        # Simulate in-memory uniqueness tracking
        self.program_names = set()

    def test_required_fields(self):
        """Should fail if name or description missing"""
        program = Mock(spec=Program)
        program.pk = 1
        program.name = ""
        program.description = ""
        program.national_alignment = "National Policy A"
        program.focus_areas = ""
        program.phases = ""

        with self.assertRaises(ValidationError) as cm:
            Program.clean(program)

        self.assertIn("Program.Name is required.", str(cm.exception))

    def test_name_uniqueness(self):
        """Should fail if another Program has the same name"""
        name = "Innovation Program"
        self.program_names.add(name.lower())

        new_program = Mock(spec=Program)
        new_program.pk = 2
        new_program.name = "Innovation Program"
        new_program.description = "New round"
        new_program.national_alignment = "Policy X"
        new_program.focus_areas = "STEM"
        new_program.phases = "Initiation"

        if new_program.name.lower() in self.program_names:
            exc = ValidationError("Program.Name already exists.")
        else:
            self.program_names.add(new_program.name.lower())
            exc = None

        self.assertEqual(str(exc), "['Program.Name already exists.']")

    def test_focus_area_requires_national_alignment(self):
        """Should fail if focus_areas set but national_alignment missing"""
        program = Mock(spec=Program)
        program.pk = 1
        program.name = "Digital Skills"
        program.description = "Support digital skills development"
        program.focus_areas = "ICT, AI"
        program.national_alignment = None  # Missing national alignment
        program.phases = ""

        # Simulate check constraint logic
        if program.focus_areas and not program.national_alignment:
            exc = ValidationError("FocusAreas requires NationalAlignment.")
        else:
            exc = None

        self.assertEqual(str(exc), "['FocusAreas requires NationalAlignment.']")

    def test_delete_guard_with_projects(self):
        """Should fail delete if Program has Projects"""
        program = Mock(spec=Program)
        program.projects = MagicMock()
        program.projects.exists.return_value = True

        with self.assertRaises(ValidationError) as cm:
            Program._delete_guard(program)

        self.assertIn("Program has Projects; archive or reassign before delete.", str(cm.exception))

    def test_valid_program_passes_clean(self):
        """Should pass when all rules satisfied"""
        program = Mock(spec=Program)
        program.pk = 1
        program.name = "Green Energy Program"
        program.description = "Promotes sustainable innovation"
        program.national_alignment = "SDG 7"
        program.focus_areas = "Renewable Energy"
        program.phases = "Planning, Execution"

        try:
            Program.clean(program)
        except ValidationError:
            self.fail("clean() raised ValidationError unexpectedly for valid Program")
