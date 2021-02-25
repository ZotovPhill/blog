from django.db import models

from blog.models.acl.ability import Ability
from blog.models.base_model import BaseModel
from blog.models.blog.blog import Blog


class Role(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    abilities = models.ManyToManyField(Ability)

    class Meta:
        db_table = 'acl_role'

    def has_ability(self):
        pass

    def show_role_abilities(self):
        pass
