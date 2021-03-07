from django.db import models
from django.template.defaultfilters import slugify

from blog.models.acl.ability import Ability
from blog.models.base_model import BaseModel
from blog.models.blog.blog import Blog


class Role(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    abilities = models.ManyToManyField(Ability)

    class Meta:
        db_table = 'acl_role'
        unique_together = ('blog', 'code')

    def has_abilities(self, abilities: list):
        pass

    def show_role_abilities(self):
        return [ability for ability in self.abilities.all()]

    def save(self, *args, **kwargs):
        if not self.id:
            self.code = slugify(self.name)
        super(Role, self).save(*args, **kwargs)
