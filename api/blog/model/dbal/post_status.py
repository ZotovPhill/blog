from django.db import models
from django.utils.translation import gettext_lazy as _


class PostStatus(models.TextChoices):
    DELETED = 'DELETED', _('DELETED')
    DRAFT = 'DRAFT', _('Draft')
    POSTED = 'POSTED', _('Posted')
    ARCHIVED = 'ARCHIVED', _('Archived')
    NEW = 'NEW', _('New')
