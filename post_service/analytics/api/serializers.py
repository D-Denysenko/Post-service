from rest_framework import serializers


class LikeAnaliticsPerUserOutputSerializer(serializers.Serializer):
    date = serializers.DateTimeField(source="day")
    likes_count = serializers.IntegerField()
