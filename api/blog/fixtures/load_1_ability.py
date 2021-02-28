from factory import faker
from factory.django import DjangoModelFactory
from blog.models.acl.ability import Ability


class LoadAbility(DjangoModelFactory):
    name = faker.Faker('job')
    code = faker.Faker('isbn10')

    class Meta:
        model = Ability
