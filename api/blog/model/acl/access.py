from django.db import models

from blog.model.acl.role import Role
from blog.model.base_model import BaseModel
from blog.model.blog.blog import Blog
from blog.model.profile.user import User


class Access(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
