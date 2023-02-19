from rest_framework.serializers import ModelSerializer
from app import models

class CreatePostsSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields = [
            'title','thumbnail','main_image','description','content'
        ]

class PostListSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('__all__')