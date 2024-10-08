from django.shortcuts import render
from rest_framework import generics, permissions
from new_database.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
