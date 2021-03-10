import factory
from apps.home.models import HomeText
from factory.django import DjangoModelFactory
from apps.core.models import Language


class HomeTextFactory(DjangoModelFactory):

    class Meta:
        model = HomeText

    title = factory.Faker('paragraph')
    main_text = factory.Faker('paragraph')
    secondary_text = factory.Faker('paragraph')
    language = factory.Iterator(Language.objects.all())
