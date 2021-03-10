from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from blog.models.base_model import BaseModel
from blog.models.blog.blog import Blog
from blog.models.dbal.post_status import PostStatus
from blog.models.dbal.visibility_type import VisibilityType
from blog.models.post.post_content import PostContent
from blog.models.profile.user import User


class Post(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.OneToOneField(PostContent, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    slug = models.SlugField(
        allow_unicode=True,
        unique=True,
        max_length=255,
        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/profile/[my-slug]/")
    )
    status = models.CharField(
        max_length=255,
        choices=PostStatus.choices,
        default=PostStatus.NEW
    )
    visibility = models.CharField(
        max_length=255,
        choices=VisibilityType.choices,
        default=VisibilityType.PUBLIC
    )
    published_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'blg_post'


@receiver(post_save, sender=Post)
def save_user_profile(sender, instance, **kwargs):
    instance.content.save()
