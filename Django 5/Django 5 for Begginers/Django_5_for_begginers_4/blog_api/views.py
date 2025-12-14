from django_filters.rest_framework import DjangoFilterBackend  # new
from rest_framework import generics

from blog.models import Post
from .serializers import PostSerializer
from django.db.models import Sum

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]  # new
    filterset_fields = ['author']  # new


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.kwargs['id']
        Post.objects.aggregate(Sum())
        return Post.objects.filter(author=user)