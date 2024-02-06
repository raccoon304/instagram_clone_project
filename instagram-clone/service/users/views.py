# view set은 실제 요청을 처리하고 응답을 보내는 곳임 

# django modules 
from django.contrib.auth import authenticate 
from django.contrib.auth import login 

# drf modules 
from rest_framework import status
from rest_framework import Response 
from rest_framework import ModelViewSets
from rest_framework.permissions import AllowAny 

# models 
from users.models import User 

# serializers 
from users.serializers import UserSerializer

class AuthViewSet(ModelViewSets):
    #쿼리셋은 다수의 유저 동작을 할때 필요 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = [AllowAny]
    
#0911