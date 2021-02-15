from django.core.validators import URLValidator, MinValueValidator
from django.db import models

from blog.model.base_model import BaseModel


class FileReference(BaseModel):
    path = models.CharField(max_length=255, null=False, validators=[URLValidator])
    mime_type = models.CharField(max_length=255, null=False)
    extension = models.CharField(max_length=255, null=False)
    size = models.IntegerField(validators=[MinValueValidator(0)])
    original_name = models.CharField(max_length=255, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'fl_file_reference'
