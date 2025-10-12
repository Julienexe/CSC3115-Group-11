import factory
from faker import Faker
from facilities.models import Facility, Service, Equipment

fake = Faker()

class FacilityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Facility

    name = factory.LazyFunction(fake.company)
    location = factory.LazyFunction(fake.city)
    facility_type = factory.Iterator(["lab", "workshop", "testing"])
    description = factory.LazyFunction(fake.text)
    partner_organization = factory.LazyFunction(fake.company)
    capabilities = factory.LazyFunction(lambda: fake.sentence())

class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = factory.LazyFunction(fake.bs)
    description = factory.LazyFunction(fake.text)
    facility = factory.SubFactory(FacilityFactory)
    category = factory.Iterator(["machining", "testing", "training"])
    skill_type = factory.Iterator(["hardware", "software", "integration"])

class EquipmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Equipment

    name = factory.LazyFunction(fake.word)
    capabilities = factory.LazyFunction(lambda: fake.sentence())
    description = factory.LazyFunction(fake.text)
    inventory_code = factory.LazyFunction(lambda: fake.unique.bothify(text='??-#####'))
    usage_domain = factory.Iterator(["electronics", "mechanical", "iot", "robotics", "software"])
    support_phase = factory.Iterator(["training", "prototyping", "testing", "commercialization"])
    facility = factory.SubFactory(FacilityFactory)
