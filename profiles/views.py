from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfieSerializer
from rest_framework import generics
from new_database.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    serializer_class = ProfieSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all().order_by('-created_at')

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfieSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()