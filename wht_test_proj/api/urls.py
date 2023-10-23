from django.urls import path
from .views import TeamListCreateView, UserListCreateView, UserUpdateDestroyAPIView, TeamUpdateDestroyAPIView

app_name = 'api'

urlpatterns = [
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamUpdateDestroyAPIView.as_view(), name='team-update-destroy'),

    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserUpdateDestroyAPIView.as_view(), name='user-update-destroy'),
]
