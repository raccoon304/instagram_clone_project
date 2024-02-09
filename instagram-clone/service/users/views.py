# view set은 실제 요청을 처리하고 응답을 보내는 곳임 

# django modules 
from django.contrib.auth import authenticate 
from django.contrib.auth import login 

# drf modules 
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny 

# models 
from users.models import User 

# serializers 
from users.serializers import UserSerializer

class AuthViewSet(ModelViewSet):
    #쿼리셋은 다수의 유저 동작을 할때 필요 
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ AllowAny ]
    authentication_classes = []
    
    
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        #회원가입시 두가지 동작이 있는데 1. 회원가입 후 바로 로그인 되어지는 경우 / 2. 회원가입 후 로그인을 새로 해야하는 경우 
        # 해당 프로젝트에서는 회원가입후 바로 로그인 되는 서비스를 이용
        login(request, user)
        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
        )
        