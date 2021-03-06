from typing import Union

from django.template.defaultfilters import slugify

from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models import Tag


class LoadTag(AbstractFixtureLoader):
    def load(self, quantity: Union[int, None] = None, is_catalog: bool = False) -> None:
        tags_list = []
        for _ in range(quantity):
            tag_name = self.fake.sentence(nb_words=4, variable_nb_words=True)
            tags_list.append(Tag(name=tag_name, slug=slugify(tag_name)))
        for i in range(0, len(tags_list), self.BATCH_SIZE):
            Tag.objects.bulk_create(tags_list[i:i+self.BATCH_SIZE])

    def env_group(self) -> list:
        return ['dev', 'prod']
