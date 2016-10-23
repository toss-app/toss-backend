from ..models import Account

from .serializers import AccountSerializer, BasicAccountSerializer

from django.contrib.auth import get_user_model, authenticate
from django.db.models import Q

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
            queryset = get_user_model().objects.filter(id=user.id)
            return queryset
        return get_user_model().objects.none() 

    def get_filtered_queryset(self):
        queryset = get_user_model().objects.all()
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(Q(username__icontains=name_filter) 
                                       | Q(first_name__icontains=name_filter)
                                       | Q(last_name__icontains=name_filter))
        limit_filter = self.request.query_params.get('limit', None)
        if limit_filter is not None and self.represents_int(limit_filter):
            queryset = queryset[0:int(limit_filter)]
        return queryset


    def list(self, request):
        users = BasicAccountSerializer(self.get_filtered_queryset(), many=True)
        return Response(users.data)

    def retrieve(self, request, pk):
        user = BasicAccountSerializer(self.get_filtered_queryset().get(pk=pk))
        return Response(user.data)

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

    def represents_int(self, str):
        try: 
            int(str)
            return True
        except ValueError:
            return False
