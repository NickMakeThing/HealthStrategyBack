from django.shortcuts import render
from django.views.generic.edit import CreateView
from app.models import Post
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView
from .serializers import CreatePostsSerializer, PostListSerializer

# class AuthorCreateView(CreateView):
#     model = Post
#     fields = ['title','date','thumbnail','main_image','content']
#     # for content, it will be a dict that is turned into json with
#     # type, content
class CreatePosts(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostsSerializer
    
class GetAllBlogPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    # need to add pagination for when too many posts accumulate

class GetBlogPost(RetrieveAPIView):
    pass


# class HomeView(TemplateView):
#     pass
# do this in urls https://docs.djangoproject.com/en/4.1/topics/class-based-views/
