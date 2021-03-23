from rest_framework import serializers

from blog.models import PostContent, Tag, Post, Blog
from blog.serializers.base_model_serializer import BaseModelSerializer


class ShortPostContent(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display', read_only=True)
    description = serializers.CharField(
        source='get_short_description',
        read_only=True,
    )

    class Meta:
        model = PostContent
        fields = ('id', 'type', 'title', 'description', 'external_link',)


class ShortTag(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'get_name',)


class ShortBlog(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title',)


class ShortPost(BaseModelSerializer):
    blog = ShortBlog()
    tags = ShortTag(many=True)
    content = ShortPostContent()

    class Meta:
        model = Post
        fields = ('id', 'blog', 'tags', 'content', 'published_at',)
