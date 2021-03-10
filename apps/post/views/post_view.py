from rest_framework.response import  Response
from rest_framework.views import APIView
from apps.post.serializers import PostSerializer
from apps.post.models import Post


class PostView(APIView):

    def get(self, request):
        lang = request.GET.get('lang', 'en')
        posts = Post.objects.get(language__code=lang)

        post_serializer = PostSerializer(posts, many=True)
        return Response(post_serializer.data)