from django.db import models

from blog.model.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _


class Ability(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    code = models.CharField(verbose_name=_('code'), max_length=255)

    class Meta:
        db_table = 'acl_ability'

