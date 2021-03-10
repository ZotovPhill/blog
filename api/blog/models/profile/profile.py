from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from blog.models.base_model import BaseModel
from blog.models.file.file import File
from blog.models.profile.user import User


class Profile(BaseModel):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    username = models.CharField(
        max_length=255,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(
        allow_unicode=True,
        max_length=255,
        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/profile/[my-slug]/")
    )
    photo = models.OneToOneField(
        File,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        db_table = 'pa_profile'

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
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
