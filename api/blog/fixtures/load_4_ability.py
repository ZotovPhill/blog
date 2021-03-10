import csv
import os
from typing import Union

from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models import Role
from blog.models.acl.ability import Ability


class LoadAbility(AbstractFixtureLoader):
    def load(self, quantity: Union[int, None]) -> None:
        with open(os.path.join(self.CATALOG_FOLDER, 'abilities.csv'), 'r') as catalog:
            abilities = csv.reader(catalog, delimiter=',')
            for ability in abilities:
                ability_object = Ability.objects.create(code=ability[0], description=ability[1])
                ability_object.save()

                roles = Role.objects.filter(code__in=ability[2].split('|'))
                for role in roles:
                    role.abilities.add(ability_object)

    def env_group(self) -> list:
        return ['dev', 'prod']
