from rest_framework.response import Response
from rest_framework.views import APIView
from apps.home.models.home_text import HomeText
from apps.home.serializers import HomeTextSerializer


# Create your views here.
class HomeTextView(APIView):

    def get(self, request):
        lang = request.GET.get('lang', None)

        if lang:
            home_texts = HomeText.objects.get(language__code=lang)
        else:
            home_texts = HomeText.objects.get(language__code='en')

        home_texts_serializer = HomeTextSerializer(home_texts)
        return Response(home_texts_serializer.data)
