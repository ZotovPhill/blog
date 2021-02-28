from django.core.validators import int_list_validator
from django.db import models

from blog.models.base_model import BaseModel


class Visibility(BaseModel):
    object_id = models.CharField(max_length=255)
    object_class = models.CharField(max_length=255)
    employees = models.CharField(
        max_length=1000,
        validators=[int_list_validator],
        help_text="""Empty value means public,
                    single value for private access only,
                    and list of ids for limited access to object."""
    )

    class Meta:
        db_table = 'acl_visibility'
