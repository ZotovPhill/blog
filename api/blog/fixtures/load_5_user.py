import random
from typing import Union

from django.template.defaultfilters import slugify

from blog.fixtures.abstract_fixture_loader import AbstractFixtureLoader
from blog.models import Profile, User, Role


class LoadUser(AbstractFixtureLoader):
    INITIAL_PASSWORD = 'ZxCqWe135'

    def load(self, quantity: Union[int, None]) -> None:
        roles = Role.objects.all()
        usernames = [self.fake.user_name() for _ in range(quantity)]
        profiles = (Profile(
            username=username,
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            slug=slugify(username)
        ) for username in usernames)

        for profile in profiles:
            user = User(email=self.fake.safe_email(), profile=profile)
            user.set_password(self.INITIAL_PASSWORD)
            user.save()

            random_roles = [roles[random.randint(0, quantity)] for _ in range(3)]
            user.roles.add(*random_roles)

    def env_group(self) -> list:
        return ['dev']
