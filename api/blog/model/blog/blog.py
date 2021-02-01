from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import (
    check_password,
    make_password,
)

from blog.model.base_model import BaseModel


class Blog(BaseModel):
    title = models.CharField(verbose_name=_('title'), max_length=255, null=False)
    slug = models.SlugField(verbose_name=_('slug'), max_length=255, default=slugify(title), unique=True)
    is_private = models.BooleanField(verbose_name=_('is_private'), default=False)
    password = models.CharField(_('password'), max_length=128, null=True)
    last_modified = models.DateTimeField(verbose_name=_('last_modified'))
    last_access = models.DateTimeField(verbose_name=_('last_access'))

    _password = None

    def set_password(self, raw_password):
        if (timezone.now() - self.last_modified).days < 1:
            raise ValidationError
        password_validation.validate_password(self._password)
        self.password = make_password(raw_password)
        self._password = raw_password
        self.last_modified = timezone.now()
        self.save(update_fields=["last_modified", "password"])

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self._password = None
            self.save(update_fields=["password"])
        valid = check_password(raw_password, self.password, setter)
        self.last_access = timezone.now()
        self.save(update_fields=["last_access"])
        return valid

    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)
        if self._password is not None:
            self.check_password(raw_password=self._password)
            self._password = None


@receiver(pre_save, sender=Blog)
def change_slug_on_title_modify(sender, instance, **kwargs):
    if instance.id is None:
        blog = sender.objects.get(title=instance.title)
        if isinstance(blog, Blog):
            raise models.ProtectedError("Title already exist, and cannot be modified")
    else:
        previous = sender.objects.get(pk=instance.id)
        if previous.title != instance.title:
            instance.slug = slugify(instance.title, allow_unicode=True)
    instance.save()
