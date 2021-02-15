from django.db import models
from django.utils.translation import ugettext_lazy as _

from blog.model.base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=255, unique=True, blank=False)
    slug = models.SlugField(
        verbose_name=_('slug'),
        allow_unicode=True,
        unique=True,
        max_length=255,
        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/profile/[my-slug]/")
    )

    class Meta:
        db_table = 'blg_tag'
