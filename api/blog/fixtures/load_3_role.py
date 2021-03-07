import csv
import os
from itertools import islice
from typing import Union

from django.template.defaultfilters import slugify

from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models import Role, Blog


class LoadRole(AbstractFixtureLoader):
    def load(self, quantity: Union[int, None] = None, is_catalog: bool = False) -> None:
        with open(os.path.join(self.CATALOG_FOLDER, 'roles.csv'), 'r') as catalog:
            roles = csv.reader(catalog, delimiter=',')
            for role in roles:
                blogs = Blog.objects.filter(id__in=role[1].split('|'))
                objs = (Role(name=role[0], blog=blog, code=slugify(role[0])) for blog in blogs)
                while True:
                    batch = list(islice(objs, self.BATCH_SIZE))
                    if not batch:
                        break
                    Role.objects.bulk_create(batch, self.BATCH_SIZE)

    def env_group(self) -> list:
        return ['dev']