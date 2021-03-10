from django.core.management import BaseCommand, CommandError
from apps.post.factories import PostFactory
from apps.core.factories import LanguageFactory
from django.db import transaction


class Command(BaseCommand):
    help = 'Populate post table'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help="quantity of post to create")

    def handle(self, *args, **kwargs):
        try:
            if kwargs['quantity']:
                quantity = kwargs['quantity']
            else:
                quantity = 5

            with transaction.atomic():
                for _ in range(quantity):
                    self._load_fixtures()
        except Exception as e:
            raise CommandError(f'{e}\n\nTransaction doesn\' complete by a exception')

    def _load_fixtures(self):
        PostFactory.create()

