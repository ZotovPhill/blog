from typing import Union

from django.template.defaultfilters import slugify

from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models import Blog


class LoadBlog(AbstractFixtureLoader):
    INITIAL_PASSWORD = 'ZxCqWe135'

    def load(self, quantity: Union[int, None]) -> None:
        blog_list = []
        counter = 0
        for _ in range(quantity):
            title = self.fake.sentence(nb_words=4, variable_nb_words=True)
            is_private = True if counter % 4 == 0 else False
            blog = Blog(title=title, slug=slugify(title), is_private=is_private)
            if counter % 6 == 0:
                blog = blog.set_initial_password(self.INITIAL_PASSWORD)
            blog_list.append(blog)
            counter += 1
            if counter == self.BATCH_SIZE:
                Blog.objects.bulk_create(blog_list)
                blog_list = []
                counter = 0
        Blog.objects.bulk_create(blog_list)

    def env_group(self) -> list:
        return ['dev']
