from django.core.checks import Tags
from django.db import models
from django.utils.translation import ugettext_lazy as _

from blog.model.base_model import BaseModel
from blog.model.blog.blog import Blog
from blog.model.dbal.post_status import PostStatus
from blog.model.post.post_content import PostContent
from blog.model.profile.profile import Profile


class Post(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.ForeignKey(PostContent, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    slug = models.SlugField(
        verbose_name=_('slug'),
        allow_unicode=True,
        unique=True,
        max_length=255,
        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/profile/[my-slug]/")
    )
    status = models.CharField(
        verbose_name=_('status'),
        max_length=30,
        choices=PostStatus.choices,
        default=PostStatus.NEW
    )
    published_at = models.DateTimeField(verbose_name=_('published_at'))

    class Meta:
        db_table = 'blg_post'
