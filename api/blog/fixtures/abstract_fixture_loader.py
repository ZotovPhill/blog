import os
from abc import ABCMeta, abstractmethod
from typing import Union

import faker
from django.apps import apps


class AbstractFixtureLoader(metaclass=ABCMeta):
    BATCH_SIZE = 100
    CATALOG_FOLDER = os.path.join(apps.get_app_config('blog').path, 'fixtures', 'catalog')

    def __init__(self):
        self.fake = faker.Faker()

    @abstractmethod
    def load(self, quantity: Union[int, None]) -> None:
        pass

    @abstractmethod
    def env_group(self) -> list:
        return []
