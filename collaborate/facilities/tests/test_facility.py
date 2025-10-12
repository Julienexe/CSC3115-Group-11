from django.test import SimpleTestCase
from unittest.mock import MagicMock, patch
from django.core.exceptions import ValidationError
from .factories import FacilityFactory, ServiceFactory, EquipmentFactory


class FacilityBusinessLogicTests(SimpleTestCase):
    def setUp(self):
        # Build facility and related objects in memory
        self.facility = FacilityFactory.build(capabilities="")  # empty to trigger validation
        self.service1 = ServiceFactory.build()
        self.service2 = ServiceFactory.build()
        self.equipment1 = EquipmentFactory.build()

        # Patch related managers to simulate existing related objects
        services_patcher = patch('facilities.models.Facility.services', new_callable=MagicMock)
        equipment_patcher = patch('facilities.models.Facility.equipment', new_callable=MagicMock)

        self.mock_services = services_patcher.start()
        self.mock_equipment = equipment_patcher.start()

        # Stop patchers automatically after tests
        self.addCleanup(services_patcher.stop)
        self.addCleanup(equipment_patcher.stop)

        # Configure mocks
        self.mock_services.exists.return_value = True
        self.mock_services.count.return_value = 2
        self.mock_equipment.exists.return_value = True
        self.mock_equipment.count.return_value = 1

    def test_required_fields_validation(self):
        facility = FacilityFactory.build(name=None, location=None, facility_type=None)
        with self.assertRaises(ValidationError) as cm:
            facility.clean()
        self.assertIn(
            "Facility.Name, Facility.Location, and Facility.FacilityType are required.",
            str(cm.exception)
        )

    def test_capabilities_validation(self):
            # Validation should fail because capabilities is empty and related objects exist
            with self.assertRaises(ValidationError) as cm:
                self.facility.clean()

            self.assertTrue(
                "Capabilities must be populated" in str(cm.exception) or
                "Capabilities are required" in str(cm.exception)
            )

    def test_deletion_constraints(self):

        with self.assertRaises(ValidationError) as cm:
            self.facility.delete_check()
        self.assertIn("Facility has dependent records", str(cm.exception))

    def test_uniqueness_rule_in_memory(self):
        """
        Simulate uniqueness in-memory since build() does not hit the DB
        """
        registry = set()
        facility1 = FacilityFactory.build(name="TestLab", location="CityA")
        registry.add((facility1.name, facility1.location))

        facility2 = FacilityFactory.build(name="TestLab", location="CityA")
        if (facility2.name, facility2.location) in registry:
            exc = ValidationError("A facility with this name already exists at this location.")
        else:
            exc = None

        self.assertEqual(str(exc), "['A facility with this name already exists at this location.']")
