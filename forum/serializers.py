from .models import User, Comment
from rest_framework import serializers, exceptions

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'date', 'body')

    def create(self, validated_data):
        comment = Comment.objects.create(
            user = validated_data['user'],
            date = validated_data['date'],
            body = validated_data['body'],
        )
        comment.save()
        return comment