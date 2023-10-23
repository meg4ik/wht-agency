from django.urls import path
from .views import TeamListCreateView, UserListCreateView

app_name = 'api'

urlpatterns = [
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
]
