import os
import sys
import tracemalloc
import textwrap
import yaml
import importlib

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.db import transaction
from django.conf import settings
from factory.django import DjangoModelFactory


class Command(BaseCommand):
    help = "Load fixtures of given model (by default load fixtures of all models)"
    requires_migrations_checks = True

    def add_arguments(self, parser):
        # parser.add_argument('-d', '--drop', nargs='*')
        pass

    def handle(self, *args, **options):
        question = input(self.style.HTTP_NOT_MODIFIED(textwrap.fill(
            "This command will drop all your data and generate new "
            "fixtures. Would you like to continue? (yes / no) ", 55
        )))
        if question.lower() == "no":
            sys.exit()

        # Load models that presented in config file fixtures.yaml
        load_models = self.load_models_from_config()

        # WARNING. Clear all tables.
        models_klass = [model['class']._meta.model for model in load_models.values()]
        self._truncate_db(models_klass)

        tracemalloc.start()

        for model in load_models.values():
            self._fill_db(model['class'], model['attributes'])

        current, peak = tracemalloc.get_traced_memory()
        self.stdout.write(self.style.SUCCESS(f"\nSuccessfully loaded all {len(load_models)} fixtures!"))
        self.stdout.write(
            self.style.HTTP_SUCCESS(f"Current memory usage: {current / 10 ** 3} KB; Peak usage: {peak / 10 ** 3} KB")
        )

    def _truncate_db(self, models: list) -> None:
        for model in models:
            model.truncate()
        self.stdout.write(self.style.SUCCESS("Successfully deleted data from tables!\n"))

    @transaction.atomic
    def _fill_db(self, model: DjangoModelFactory, attrs: dict) -> None:
        try:
            if 'catalog' not in attrs.keys() or not attrs['catalog']:
                model.create_batch(attrs.get('quantity', 100))
            else:
                model.create()
        except Exception as e:
            self.stderr.write(f"Error processing {model} fixture: \n {e}")
        self.stdout.write(self.style.SUCCESS(f"{model.__name__.capitalize()} fixtures loaded successfully"))

    @staticmethod
    def load_models_from_config() -> dict:
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
                load_models = {}
                base_dir = config['fixtures']['base_dir']
                models = config['fixtures'].get('load', {})
                for model in models.values():
                    module = importlib.import_module(f"{base_dir}.{model['module']}")
                    load_models[model['class']] = {
                        'class': getattr(module, model['class']),
                        'attributes': model.get('attributes', {})
                    }
            except (yaml.MarkedYAMLError, KeyError, AttributeError) as exc:
                raise CommandError('Configuration file error: ' + exc)
        return load_models
