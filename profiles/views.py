from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfieSerializer
from rest_framework import generics, filters
from new_database.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

class ProfileList(generics.ListAPIView):
    serializer_class = ProfieSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        post_count = Count('owner__post', distinct=True),
        follower_count = Count('owner__follows', distinct=True),
        following_count = Count('owner__followed', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    ordering_fields = [
        'post_count',
        'following_count',
        'follower_count',
        'owner__followed__created_at',
        'owner__follows__created_at',
    ]

    search_fields = [
        'owner__username',
    ]

    filterset_fields = [
        'owner__profile',
    ]

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfieSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()