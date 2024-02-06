from rest_framework import serializers

from models import User

# 이 시리얼 라이저는 유저필드의 데이터들로 JSON을 생성하게 해줌 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = (
            'pk',
            'email',
            'username',
            'profile',
            'description',
            'password',
            'updated'
        )
        #password를 쓰기에서만 사용하기 위해 extra_kwargs를 정의함 
        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }
        
        def create(self, validated_data):
            # 앞어 정의한 매니저에 크리에이트 유저를 사용하여 사용자 객체를 생성해서 반환함 
            return User.objects.create_user(**validated_data)
        