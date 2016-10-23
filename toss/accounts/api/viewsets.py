from ..models import Account

from .serializers import AccountSerializer

from django.contrib.auth import get_user_model, authenticate

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.authtoken.models import Token

class AccountViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)
    serializer_class = AccountSerializer

    def get_queryset(self):
        user = TokenAuthentication().authenticate(self.request)
        if user is not None:
            user = user[0]
            if user.is_superuser:
                return get_user_model().objects.all()
            else:
                return get_user_model().objects.filter(id=user.id)
        return get_user_model().objects.none() 

    @list_route(methods=["POST"], url_path="login")
    def login(self, request):
        # validate to check if the data is even there
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                token = Token.objects.get(user=user)
                return Response({ "token": token.key })
            else:
                return Response(data={"Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)

