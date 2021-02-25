import uuid as uuid

from django.db import models
from blog.models.base_model import BaseModel
from blog.models.dbal.file_status import FileStatus
from blog.models.dbal.file_type import FileType
from blog.models.dbal.visibility_type import VisibilityType
from blog.models.file.file_reference import FileReference
from blog.models.profile.user import User


class File(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    status = models.CharField(
        max_length=255,
        choices=FileStatus.choices,
        default=FileStatus.NEW
    )
    type = models.CharField(max_length=255, choices=FileType.choices, default=FileType.IMAGE)
    visibility = models.CharField(
        max_length=255,
        choices=VisibilityType.choices,
        default=VisibilityType.PUBLIC
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    file_reference = models.ForeignKey(FileReference, on_delete=models.CASCADE)
    is_temp = models.BooleanField(default=False)

    class Meta:
        db_table = 'fl_file'
