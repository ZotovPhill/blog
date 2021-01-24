from django.db import models

from blog.model.acl.ability import Ability
from blog.model.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _


class Role(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    code = models.CharField(verbose_name=_('code'), max_length=255)
    abilities = models.ManyToManyField(Ability)

    def has_ability(self):
        pass

    def show_role_abilities(self):
        pass
