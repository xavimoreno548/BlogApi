import factory
from apps.post.models import Post
from apps.core.models import Language
from factory.django import DjangoModelFactory, ImageField
from django.core.files.base import ContentFile


class PostFactory(DjangoModelFactory):

    class Meta:
        model = Post

    title = factory.Faker('paragraph')
    body = factory.Faker('paragraph')
    image = factory.LazyAttribute(
            lambda _: ContentFile(
                ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'example.jpg'
            )
        )
    language = factory.Iterator(Language.objects.all())
