from django.db import models

from blog.models.base_model import BaseModel


class Ability(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        db_table = 'acl_ability'
