from django.db import models
from django.utils.translation import ugettext_lazy as _
from blog.model.base_model import BaseModel
from blog.model.file.file_reference import FileReference
from blog.model.profile.profile import Profile


class File(BaseModel):
    uuid = models.UUIDField()
    name = models.CharField()
    status = models.CharField()
    type = models.CharField()
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    file_reference = models.ForeignKey(
        FileReference,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    is_temp = models.BooleanField(verbose_name=_('is_temp'), default=False)

    class Meta:
        db_table = 'fl_file'
