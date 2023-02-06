from rest_framework import serializers

from post_service.posts.models import Post


class CreatePostInputSerializer(serializers.Serializer):
    text = serializers.CharField()


class CreatePostOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "edited", "text"]


class RetrievePostOutputSerializer(serializers.ModelSerializer):
    count_likes = serializers.IntegerField()
    count_unlikes = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ["id", "edited", "text", "count_likes", "count_unlikes"]


class ListPostsOutputSerializer(serializers.ModelSerializer):
    actor_id = serializers.UUIDField(source="actor.id")

    class Meta:
        model = Post
        fields = ["actor_id", "id", "edited", "text"]
