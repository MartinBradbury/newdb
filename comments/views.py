from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import generics
from new_database.permissions import IsOwnerOrReadOnly

class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all().order_by('-created_at')

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()