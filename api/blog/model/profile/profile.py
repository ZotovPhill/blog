from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from blog.model.base_model import BaseModel
from blog.model.profile.user import User


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(
        verbose_name=_('username'),
        max_length=255,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(verbose_name=_('first name'), max_length=255, blank=True)
    last_name = models.CharField(verbose_name=_('last name'), max_length=255, blank=True)

    slug = models.SlugField(
        verbose_name=_('slug'),
        allow_unicode=True,
        max_length=255,
        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/profile/[my-slug]/")
    )
    photo = models.OneToOneField(
        'File',
        verbose_name=_('photo'),
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
    )

    def save(self, *args, **kwargs):
        """
        Slugify and normalize username for profile url slug usage
        """
        if self.id and self.username:
            self.slug = slugify(self.username, allow_unicode=True)
        super(Profile, self).save(*args, **kwargs)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Hooking User model method. Call on User model create.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Hooking User model method. Call on User model update.
    """
    instance.profile.save()


