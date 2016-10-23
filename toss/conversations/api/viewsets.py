from ..models import Conversation
from .serializers import ConversationSerializer
from helpers.api.viewsets import AuthenticatedModelViewSet

class ConversationViewSet(AuthenticatedModelViewSet):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()
    

