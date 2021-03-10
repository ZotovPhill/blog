import os
import re
import sys
import tracemalloc
import textwrap
import yaml
import importlib

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.db import transaction
from django.conf import settings


class Command(BaseCommand):
    help = "Load fixtures for models described in the fixtures.yaml file."
    requires_migrations_checks = True

    successful_load = 0

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-interaction",
            action="store_true",
            help="Pointing this argument for no disable interactions and "
                 "console input. WARNING! Automatic consent to the deletion"
                 " of all data and database and applying fixtures."
        )

    def handle(self, *args, **options):
        if not options['no_interaction']:
            question = input(self.style.HTTP_NOT_MODIFIED(textwrap.fill(
                "This command will drop all your data and generate new "
                "fixtures. Would you like to continue? (yes / no): ", 55
            )))
            if not re.search('(y|yes)', question.lower()):
                sys.exit()

        # Load models that presented in config file fixtures.yaml
        load_fixtures = self.load_fixtures_from_config()

        tracemalloc.start()

        for fixture in load_fixtures.values():
            self._fill_db(fixture['class'], fixture['attributes'])

        current, peak = tracemalloc.get_traced_memory()
        self.stdout.write(self.style.SUCCESS(f"\nSuccessfully loaded {self.successful_load} fixtures!"))
        self.stdout.write(
            self.style.HTTP_SUCCESS(f"Current memory usage: {current / 10 ** 3} KB; Peak usage: {peak / 10 ** 3} KB")
        )

    @transaction.atomic
    def _fill_db(self, fixture, attrs: dict) -> None:
        try:
            obj = fixture()
            if settings.ENVIRONMENT not in obj.env_group():
                return
            obj.load(attrs.get('quantity', None))
            self.successful_load += 1
        except Exception as e:
            self.stderr.write(f"Error processing {fixture.__name__} fixture: \n {e}")
            sys.exit()
        self.stdout.write(self.style.SUCCESS(f"{fixture.__name__} fixtures loaded successfully"))

    @staticmethod
    def load_fixtures_from_config() -> dict:
        with open(
            os.path.join(
                apps.get_app_config('blog').path,
                'config',
                settings.ENVIRONMENT,
                'fixtures.yaml'
            )
        ) as config:
            try:
                config = yaml.safe_load(config)
                load_fixtures = {}
                base_dir = config['fixtures']['base_dir']
                fixture_classes = config['fixtures'].get('load', {})
                for fixture in fixture_classes.values():
                    module = importlib.import_module(f"{base_dir}.{fixture['module']}")
                    load_fixtures[fixture['class']] = {
                        'class': getattr(module, fixture['class']),
                        'attributes': fixture.get('attributes', {})
                    }
            except (yaml.MarkedYAMLError, KeyError, AttributeError) as exc:
                raise CommandError('Configuration file error: ' + exc)
        return load_fixtures
