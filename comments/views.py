from .models import Comment
from .serializers import CommentSerializer
from rest_framework import generics, permissions, filters
from new_database.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.annotate(
        comment_created_at=Count('created_at', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]   

    ordering_fields = [
        'created_at',
    ]

    search_fields = [
        'title',
        'owner__username',
        'content',

    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()