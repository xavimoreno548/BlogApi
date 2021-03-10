import factory
from apps.core.models import Language
from factory.django import DjangoModelFactory


class LanguageFactory(DjangoModelFactory):

    class Meta:
        model = Language

    class Params:
        lang_name = 'English'
        lang_code = 'es'

    name = factory.SelfAttribute(attribute_name='lang_name')
    code = factory.SelfAttribute(attribute_name='lang_code')