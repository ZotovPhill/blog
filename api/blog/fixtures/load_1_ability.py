from itertools import islice

import faker
from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models.acl.ability import Ability


class LoadAbility(AbstractFixtureLoader):
    def load(self, quantity: int = None, is_catalog: bool = False) -> None:
        objs = (Ability(description=self.fake.text(), code=self.fake.isbn10()) for _ in range(quantity))
        while True:
            batch = list(islice(objs, self.BATCH_SIZE))
            if not batch:
                break
            Ability.objects.bulk_create(batch, self.BATCH_SIZE)

    def env_group(self) -> list:
        return ['dev', 'prod']
