from typing import Union

from django.template.defaultfilters import slugify

from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models import Tag


class LoadTag(AbstractFixtureLoader):
    def load(self, quantity: Union[int, None] = None, is_catalog: bool = False) -> None:
        tags_list = []
        counter = 0
        for _ in range(quantity):
            tag_name = self.fake.sentence(nb_words=4, variable_nb_words=True)
            tags_list.append(Tag(name=tag_name, slug=slugify(tag_name)))
            counter += 1
            if counter == self.BATCH_SIZE:
                Tag.objects.bulk_create(tags_list)
                tags_list = []
                counter = 0
        Tag.objects.bulk_create(tags_list)

    def env_group(self) -> list:
        return ['dev', 'prod']
