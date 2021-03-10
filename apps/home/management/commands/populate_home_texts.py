from django.core.management import BaseCommand, CommandError
from apps.home.factories import HomeTextFactory
from apps.core.factories import LanguageFactory
from django.db import transaction


class Command(BaseCommand):
    help = "Populate home text table"

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                self._load_fixtures()
        except Exception as e:
            raise CommandError(f"{e}\n\nTransaction doesn\'t execute by a exception")

    def _load_fixtures(self):
        HomeTextFactory.create()
