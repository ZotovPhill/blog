import mimetypes

import magic
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models

from blog.models.base_model import BaseModel


def select_storage():
    return FileSystemStorage(location=settings.MEDIA_ROOT + '/public') \
        if settings.DEBUG \
        else RemoteSystemStorage()


class RemoteSystemStorage:
    pass


class FileReference(BaseModel):
    storage_file = models.FileField(storage=select_storage)
    mime_type = models.CharField(max_length=255, null=False)
    extension = models.CharField(max_length=255, null=False)
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fl_file_reference'

    def fill_file_info(self, path):
        mime_type = magic.from_file(path, mime=True)
        extension = mimetypes.guess_extension(mime_type)
        self.mime_type = mime_type
        self.extension = extension
        return self
