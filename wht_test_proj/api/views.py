from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Team
from django.contrib.auth import get_user_model
from .serializers import TeamSerializer, UserSerializer

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
