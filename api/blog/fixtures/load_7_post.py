import random
from typing import Union

from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models import Post, PostContent, File, Blog, User, Tag
from blog.models.dbal.content_type import ContentType
from blog.models.dbal.visibility_type import VisibilityType


class LoadPost(AbstractFixtureLoader):
    def load(self, quantity: Union[int, None]) -> None:
        files = File.objects.all()
        blogs = Blog.objects.all()
        users = User.objects.all()
        tags = Tag.objects.all()

        files_count = files.count()
        tags_count = tags.count()

        for _ in range(quantity):
            content = PostContent(
                type=random.choice(ContentType.choices),
                title=self.fake.sentence(nb_words=2, variable_nb_words=True),
                description=self.fake.text(),
                external_link=self.fake.url()
            )
            content.save()

            random_files = [files[random.randint(0, files_count-1)] for _ in range(3)]
            content.file.add(*random_files)

            post = Post(
                blog=random.choice(blogs),
                user=random.choice(users),
                content=content,
                slug=self.fake.slug(),
                visibility=random.choice(VisibilityType.choices)
            )
            post.save()

            random_tags = [tags[random.randint(0, tags_count-1)] for _ in range(3)]
            post.tags.add(*random_tags)

    def env_group(self) -> list:
        return ['dev']
