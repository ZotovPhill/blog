from abc import ABCMeta, abstractmethod
from typing import Union

import faker


class AbstractFixtureLoader(metaclass=ABCMeta):
    BATCH_SIZE = 100

    def __init__(self):
        self.fake = faker.Faker()

    @abstractmethod
    def load(self, quantity: Union[int, None] = None, is_catalog: bool = False) -> None:
        pass

    @abstractmethod
    def env_group(self) -> list:
        return []
