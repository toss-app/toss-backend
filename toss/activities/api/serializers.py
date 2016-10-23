from ..models import Activity

from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('author', 'title', 'date', 'location', 'id')
