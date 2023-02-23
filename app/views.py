from django.shortcuts import render
from app.models import BlogPost
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView
from .serializers import CreatePostsSerializer, GetListSerializer, GetDetailSerializer

class CreatePosts(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = CreatePostsSerializer
    
class GetAllBlogPosts(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = GetListSerializer
    # need to add pagination for when too many posts accumulate

class GetBlogPost(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = GetDetailSerializer
    lookup_field = 'title'


# class HomeView(TemplateView):
#     pass
# do this in urls https://docs.djangoproject.com/en/4.1/topics/class-based-views/
