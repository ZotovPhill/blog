import os
import shutil
from itertools import islice
import random
from typing import Union

from django.conf import settings
from django.core.files import File as StorageFile
from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models import FileReference, File, User


class LoadFile(AbstractFixtureLoader):
    PUBLIC_FOLDER = os.path.join(settings.MEDIA_ROOT, 'public')

    def load(self, quantity: Union[int, None]) -> None:
        if os.path.exists(self.PUBLIC_FOLDER):
            shutil.rmtree(self.PUBLIC_FOLDER)
        os.makedirs(self.PUBLIC_FOLDER)
        shutil.copyfile(f"{self.CATALOG_FOLDER}/test.jpg", f"{self.PUBLIC_FOLDER}/test.jpg")

        with open(f"{self.PUBLIC_FOLDER}/test.jpg", "rb") as writer:
            storage_file = StorageFile(writer)

            file_reference = FileReference.objects.create()
            file_reference.storage_file = storage_file
            file_reference.fill_file_info(writer.read(1024))
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
