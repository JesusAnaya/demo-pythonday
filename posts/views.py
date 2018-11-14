from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer


class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
