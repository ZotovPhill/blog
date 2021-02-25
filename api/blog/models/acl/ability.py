from django.db import models

from blog.models.base_model import BaseModel


class Ability(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'acl_ability'
