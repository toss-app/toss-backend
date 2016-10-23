from .serializers import ActivitySerializer
from ..models import Activity

from helpers.api.viewsets import AuthenticatedModelViewset

from rest_framework import viewsets

class ActivityViewSet(AuthenticatedModelViewset):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
