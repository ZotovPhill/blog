from django.db import models
from django.utils.translation import gettext_lazy as _


class VisibilityType(models.TextChoices):
    PUBLIC = 'PUBLIC', _('Public')
    LIMITED = 'LIMITED', _('Limited')
    PRIVATE = 'PRIVATE', _('Private')
