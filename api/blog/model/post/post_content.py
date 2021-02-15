from django.core.validators import URLValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from blog.model.base_model import BaseModel
from blog.model.dbal.content_type import ContentType
from blog.model.file.file import File


class PostContent(BaseModel):
    type = models.CharField(verbose_name=_('type'), max_length=30, choices=ContentType.choises)
    title = models.CharField(verbose_name=_('title'), max_length=255, blank=True, editable=True)
    description = models.TextField(verbose_name=_('description'), blank=True, editable=True)
    external_link = models.CharField(
        verbose_name=_('external_link'),
        max_length=255,
        blank=True,
        validators=[URLValidator]
    )
    file = models.ManyToManyField(File)

    class Meta:
        db_table = 'blg_post_content'
