from django.core.management import BaseCommand, CommandError
from apps.core.factories import LanguageFactory
from django.db import transaction


class Command(BaseCommand):

    help = "Populate Language model, with fake data"

    def handle(self, *args, **options):
        try:
            langs = ['English', 'Spanish', 'Portuguese']
            codes = ['en', 'es', 'pt']

            with transaction.atomic():
                for i in range(len(langs)):
                    self._load_fixtures(langs[i], codes[i])
        except Exception as e:
            raise CommandError(f"{e}\n\nTransaction was not committed due to the above exception.")

    def _load_fixtures(self, lang, code):
        LanguageFactory.create(lang_name=lang, lang_code=code)