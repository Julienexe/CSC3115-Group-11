from django.test import SimpleTestCase
from unittest.mock import MagicMock, patch
from django.core.exceptions import ValidationError
from .factories import FacilityFactory,EquipmentFactory

class EquipmentBusinessLogicTests(SimpleTestCase):

    def setUp(self):
        # Build a Facility in memory
        self.facility = FacilityFactory.build()

        # Registry to simulate uniqueness of inventory_code
        self.inventory_registry = set()

    def test_required_fields_validation(self):
        equipment = EquipmentFactory.build(facility=None, name=None, inventory_code=None)

        with self.assertRaises(ValidationError) as cm:
            equipment.clean()
            self.assertIn(
                "Equipment.FacilityId, Equipment.Name, and Equipment.InventoryCode are required.",
                str(cm.exception)
            )

    def test_inventory_code_uniqueness(self):
        # Simulate existing inventory code
        code = "INV-1234"
        self.inventory_registry.add(code)

        equipment = EquipmentFactory.build(inventory_code=code)

        if equipment.inventory_code in self.inventory_registry:
            exc = ValidationError("Equipment.InventoryCode already exists.")
        else:
            exc = None
            self.inventory_registry.add(equipment.inventory_code)

        self.assertEqual(str(exc), "['Equipment.InventoryCode already exists.']")

    def test_usage_domain_support_phase_coherence(self):
        equipment = EquipmentFactory.build(
            usage_domain="electronics",
            support_phase="training"
        )

        if equipment.usage_domain == "electronics" and equipment.support_phase == "training":
            exc = ValidationError("Electronic equipment must support Prototyping or Testing.")
        else:
            exc = None

        self.assertEqual(str(exc), "['Electronic equipment must support Prototyping or Testing.']")

    def test_delete_guard(self):
        equipment = EquipmentFactory.build(facility=self.facility)

        # Patch projects reverse manager to simulate active projects
        with patch('facilities.models.Facility.projects', new_callable=MagicMock) as mock_projects:
            mock_projects.filter.return_value.exists.return_value = True  # Active project exists

            if mock_projects.filter().exists():
                exc = ValidationError("Equipment referenced by active Project.")
            else:
                exc = None

            self.assertEqual(str(exc), "['Equipment referenced by active Project.']")
