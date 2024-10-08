from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, filters
from django.db.models import Count
from new_database.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        like_count = Count('likes', distinct=True),
        comment_count = Count('comment', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    ordering_fields = [
        'like_count',
        'created_at',
        'comment_count',
    ]

    search_fields = [
        'title',
        'owner__username',
    ]

    filterset_fields = [
        'owner__profile',
    ]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()