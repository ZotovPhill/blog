from django.db import models
from django.utils.translation import gettext_lazy as _


class ContentType(models.TextChoices):
    LIST = 'LIST', _('List')
    REVIEW = 'REVIEW', _('Review')
    GALLERY = 'GALLERY', _('Gallery')
    SHORT_POST = 'SHORT_POST', _('Short_Post')
    NEWS = 'NEWS', _('News')
    EXTERNAL_RESOURCE = 'EXTERNAL_RESOURCE', _('External_Resource')
    LONG_READ = 'LONG_READ', _('Long_Read')
