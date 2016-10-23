from ..models import Response
from .serializers import ResponseSerializer
from helpers.api.viewsets import AuthenticatedModelViewSet

class ResponseViewSet(AuthenticatedModelViewSet):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()
    
