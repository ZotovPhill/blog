from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from blog.models import Post
from blog.serializers.post.short_post import ShortPost


@api_view(['GET'])
def test(request):
    return Response('Hello')


class PostViewSet(ModelViewSet):
    serializer_class = ShortPost
    queryset = Post.objects.all()
