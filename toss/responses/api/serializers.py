from ..models import Response

from rest_framework import serializers

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('attending', 'account', 'conversation', 'id')
