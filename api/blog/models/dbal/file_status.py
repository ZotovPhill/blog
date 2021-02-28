from django.db import models
from django.utils.translation import gettext_lazy as _


class FileStatus(models.TextChoices):
    FAILED = 'FAILED', _('Failed')
    DELETED = 'DELETED', _('Deleted')
    UPLOADED = 'UPLOADED', _('Uploaded')
    UPLOADING = 'UPLOADING', _('Uploading')
    NEW = 'NEW', _('New')
