from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password',  'team', 'is_staff']
        extra_kwargs = {'password': {'write_only': True},
                        'is_staff': {'read_only': True}}
        

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user