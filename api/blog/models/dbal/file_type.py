from django.db import models
from django.utils.translation import gettext_lazy as _


class FileType(models.TextChoices):
    IMAGE = 'IMAGE', _('Image')
    DOCUMENT = 'DOCUMENT', _('Document'),
    AUDIO = 'AUDIO', _('Audio')
    VIDEO = 'VIDEO', _('Video')
    PHOTO = 'PHOTO', _('Photo')
