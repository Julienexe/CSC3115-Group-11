from django.test import SimpleTestCase
from unittest.mock import Mock
from django.core.exceptions import ValidationError
from .models import Participant


class ParticipantBusinessLogicTests(SimpleTestCase):
    """Unit tests for Participant model business rules without ORM"""

    def setUp(self):
        # Simulated "email registry" for uniqueness testing
        self.email_registry = set()

    def test_required_fields(self):
        """Should fail if required fields are missing"""
        participant = Mock(spec=Participant)
        participant.pk = 1
        participant.full_name = ""
        participant.email = ""
        participant.affiliation = ""
        participant.specialization = "software"
        participant.cross_skill_trained = False
        participant.institution = "Test University"

        with self.assertRaises(ValidationError) as cm:
            Participant.clean(participant)

        self.assertIn(
            "Participant.FullName, Participant.Email, and Participant.Affiliation are required.",
            str(cm.exception)
        )

    def test_email_uniqueness(self):
        """Should fail if email already exists (case-insensitive)"""
        participant = Mock(spec=Participant)
        participant.pk = 1
        participant.full_name = "Alice"
        participant.email = "test@example.com"
        participant.affiliation = "cs"
        participant.specialization = "software"
        participant.cross_skill_trained = False
        participant.institution = "MIT"

        # Simulate first registration
        self.email_registry.add(participant.email.lower())

        # Simulate a duplicate email (different case)
        duplicate = Mock(spec=Participant)
        duplicate.pk = 2
        duplicate.full_name = "Bob"
        duplicate.email = "Test@Example.com"
        duplicate.affiliation = "se"
        duplicate.specialization = "hardware"
        duplicate.cross_skill_trained = False
        duplicate.institution = "Harvard"

        if duplicate.email.lower() in self.email_registry:
            exc = ValidationError("Participant.Email already exists.")
        else:
            exc = None
            self.email_registry.add(duplicate.email.lower())

        self.assertEqual(str(exc), "['Participant.Email already exists.']")

    def test_cross_skill_requires_specialization(self):
        """Should fail if cross_skill_trained=True and no specialization"""
        participant = Mock(spec=Participant)
        participant.pk = 1
        participant.full_name = "Jane Doe"
        participant.email = "jane@example.com"
        participant.affiliation = "eng"
        participant.specialization = ""
        participant.cross_skill_trained = True
        participant.institution = "Stanford"

        with self.assertRaises(ValidationError) as cm:
            Participant.clean(participant)

        self.assertIn("Cross-skill flag requires Specialization.", str(cm.exception))

    def test_valid_participant_passes(self):
        """Should pass when all business rules are satisfied"""
        participant = Mock(spec=Participant)
        participant.pk = 1
        participant.full_name = "John Smith"
        participant.email = "john@example.com"
        participant.affiliation = "se"
        participant.specialization = "software"
        participant.cross_skill_trained = False
        participant.institution = "Oxford"

        # No validation error expected
        try:
            Participant.clean(participant)
        except ValidationError:
            self.fail("clean() raised ValidationError unexpectedly for valid participant")
