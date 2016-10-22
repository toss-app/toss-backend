from ..models import Account

from django.contrib.auth import get_user_model
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Account
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
