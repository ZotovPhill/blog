import os
from itertools import islice
import random
from typing import Union

from django.conf import settings
from django.core.files import File as StorageFile
from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models import FileReference, File, User


class LoadFile(AbstractFixtureLoader):
    def load(self, quantity: Union[int, None]) -> None:
        full_file_name = os.path.join(settings.MEDIA_ROOT, 'public', 'test.jpg')
        with open(full_file_name, 'rb') as writer:
            storage_file = StorageFile(writer)

            file_reference = FileReference.objects.create()
            file_reference.storage_file = storage_file
            file_reference.fill_file_info(full_file_name)
            file_reference.save()

        authors = User.objects.all()
        files = (
            File(
                name='test',
                author=random.choice(authors),
                file_reference=file_reference
            ) for _ in range(quantity)
        )
        while True:
            batch = list(islice(files, self.BATCH_SIZE))
            if not batch:
                break
            File.objects.bulk_create(batch, self.BATCH_SIZE)

    def env_group(self) -> list:
        return ['dev']
