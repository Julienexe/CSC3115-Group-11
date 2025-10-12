from django.db import models
from django.forms import ValidationError
from core.models import TimeStampedModel

class Facility(TimeStampedModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    partner_organization = models.CharField(max_length=255, blank=True, null=True)
    facility_type = models.CharField(max_length=100, choices=[
        ("lab", "Lab"),
        ("workshop", "Workshop"),
        ("testing", "Testing Center"),
    ])
    capabilities = models.TextField(help_text="e.g., CNC, PCB fabrication, materials testing")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'location'], name='unique_facility_name_location')
        ]


    def __str__(self):
        return self.name + " - " + self.location
    
    def clean(self):
        """Custom validation for facility business rules"""
        super().clean()
        
        if self.pk:  # Only validate for existing instances
            if not self.name or not self.location or not self.facility_type:
                raise ValidationError(
                    "Facility.Name, Facility.Location, and Facility.FacilityType are required."
                )
            self._validate_capabilities_requirement()

    
    def _validate_capabilities_requirement(self):
        """Check if capabilities are required and present"""
        has_services = hasattr(self, 'services') and self.services.exists()
        has_equipment = hasattr(self, 'equipment_set') and self.equipment_set.exists()
        
        if (has_services or has_equipment) and not self.capabilities.strip():
            service_count = self.services.count() if has_services else 0
            equipment_count = self.equipment_set.count() if has_equipment else 0
            
            items = []
            if service_count:
                items.append(f"{service_count} service(s)")
            if equipment_count:
                items.append(f"{equipment_count} equipment item(s)")
            
            raise ValidationError({
                "Capabilities must be populated"
            })
    
    def delete_check(self):
        for related_attr in ['services', 'equipment_set', 'projects']:
            rel = getattr(self, related_attr, None)
            if rel and rel.exists():
                raise ValidationError(
                    "Facility has dependent records (Services/Equipment/Projects)."
                )



class Service(TimeStampedModel):
    facility = models.ForeignKey(Facility, related_name="services", on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ("machining", "Machining"),
        ("testing", "Testing"),
        ("training", "Training"),
    ])
    skill_type = models.CharField(max_length=100, choices=[
        ("hardware", "Hardware"),
        ("software", "Software"),
        ("integration", "Integration"),
    ])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['facility', 'name'], name='unique_service_name_per_facility')
        ]

    def __str__(self):
        return f"{self.name} ({self.facility.name})"
    
    def clean(self):
        """Custom validation for service business rules"""
        super().clean()
        
        if self.pk:  # Only validate for existing instances
            if not self.facility_id or not self.name or not self.category or not self.skill_type:
                raise ValidationError(
                    "Service.FacilityId, Service.Name, Service.Category, and Service.SkillType are required."
                )
            #should be unique within a facility, enforced by DB constraint
            
        


class Equipment(TimeStampedModel):
    facility = models.ForeignKey(Facility, related_name="equipment", on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    capabilities = models.TextField()
    description = models.TextField()
    inventory_code = models.CharField(max_length=100, unique=True)
    usage_domain = models.CharField(
        max_length=100,
        choices=[
            ("electronics", "Electronics"),
            ("mechanical", "Mechanical"),
            ("iot", "IoT"),
            ("robotics", "Robotics"),
            ("software", "Software"),
        ]
    )
    support_phase = models.CharField(
        max_length=100,
        choices=[
            ("training", "Training"),
            ("prototyping", "Prototyping"),
            ("testing", "Testing"),
            ("commercialization", "Commercialization"),
        ]
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~(models.Q(usage_domain='electronics') & models.Q(support_phase='training')),
                name='electronics_not_for_training'
            ),
        ]

    def __str__(self):
        return f"{self.name} - {self.facility.name}"
    
    def clean(self):
        """Custom validation for equipment business rules"""
        super().clean()
        
        if self.pk:  # Only validate for existing instances
            if not self.facility_id or not self.name or not self.inventory_code:
                raise ValidationError(
                    "Equipment.FacilityId, Equipment.Name, and Equipment.InventoryCode are required."
                )
      