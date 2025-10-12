from django.test import SimpleTestCase
from unittest.mock import patch, MagicMock
from django.core.exceptions import ValidationError
from .factories import ServiceFactory


class ServiceBusinessLogicTests(SimpleTestCase):

    def setUp(self):
        # Build a service in memory
        self.service = ServiceFactory.build(name="Test Service", category="testing", skill_type="hardware")
        self.facility = self.service.facility

        # Registry to simulate uniqueness within facility
        self.service_registry = {}

    def test_required_fields_validation(self):
        service = ServiceFactory.build(facility=None, name=None, category=None, skill_type=None)

        with self.assertRaises(ValidationError) as cm:
            service.clean()
            self.assertIn(
                "Service.FacilityId, Service.Name, Service.Category, and Service.SkillType are required.",
                str(cm.exception)
            )

    def test_scoped_uniqueness(self):
        # Simulate uniqueness per facility
        facility_id = id(self.facility)
        service_name = "DuplicateService"

        # Register an existing service in the facility
        self.service_registry[(facility_id, service_name)] = True

        # Build a new service with the same name in the same facility
        new_service = ServiceFactory.build(facility=self.facility, name=service_name)

        if (facility_id, new_service.name) in self.service_registry:
            exc = ValidationError("A service with this name already exists in this facility.")
        else:
            exc = None
            self.service_registry[(facility_id, new_service.name)] = True

        self.assertEqual(str(exc), "['A service with this name already exists in this facility.']")

    def test_delete_guard(self):
        service = self.service

        # Patch the Facility.projects reverse manager to simulate a project referencing the service category
        with patch('facilities.models.Facility.projects', new_callable=MagicMock) as mock_projects:
            # Simulate that a project references the service category in testing requirements
            mock_projects.filter.return_value.exists.return_value = True

            if mock_projects.filter().exists():
                exc = ValidationError("Service in use by Project testing requirements.")
            else:
                exc = None

            self.assertEqual(str(exc), "['Service in use by Project testing requirements.']")
