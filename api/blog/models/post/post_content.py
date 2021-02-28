from django.core.validators import URLValidator
from django.db import models

from blog.models.base_model import BaseModel
from blog.models.dbal.content_type import ContentType
from blog.models.file.file import File


class PostContent(BaseModel):
    type = models.CharField(max_length=30, choices=ContentType.choices, default=ContentType.SHORT_POST)
    title = models.CharField(max_length=255, blank=True, editable=True)
    description = models.TextField(blank=True, editable=True)
    external_link = models.CharField(
        max_length=255,
        blank=True,
        validators=[URLValidator]
    )
    file = models.ManyToManyField(File)

    class Meta:
        db_table = 'blg_post_content'
