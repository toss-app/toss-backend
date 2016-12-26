from .serializers import ActivitySerializer
from ..models import Activity

from helpers.api.viewsets import AuthenticatedModelViewSet

from rest_framework import viewsets

class ActivityViewSet(AuthenticatedModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
