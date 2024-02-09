'''users/models.py를 먼저 정의 할껀데 모델을 정의하기위해 models가 필요하기도 하지만 
여기서 구현하는건 회원에대한 정보의 데이터베이스 이기에 
contrib.auth.models의 AbstratUser을 사용할것임''' 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    #create_user과 create_superuser을 따로 정의 하는 이유는 장고에서 제공해주는 usermodel을 사용하면 
    #따로 정의할 필요가 없지만 사용자를 구분하기 위한 유일한 필드로 email을 지정했기 때문에 
    #회원가입 하거나 할때 이메일을 입력받아서 할 수 있도록 따로 정의함 
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        #extra_fields에는 아래에서 정의했었던 이메일, 유저네임 이외의 값들이 들어올 수 있음을 의미 
        #여기선 따로 사용하지 않기에 active 값을 True로 지정 
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        # set_password 사용하지 않으면 사용자의 비밀번호가 그대로 데이터베이스에 저장되기에 무조건 set_password로 해줘야함 
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.set_default('is_staff', True)
        extra_fields.set_default('is_superuser', True)
        extra_fields.set_default('is_active', True)
        return self.create_user(email, password, **extra_fields)


#모델 정의 
class User(AbstractUser):
    TIMEOUT = 60 * 5 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    
    #이메일에 저장될수 있는 문자열의 크기를 제한 (256)
    # unique 속성을 True 로 하면 중복이 안됨 
    email = models.EmailField(max_length=256, unique = True)
    username = models.CharField(max_length=128, unique = True)
    password = models.CharField(max_length=128, null=True, blank = True)
    profile = models.ImageField(null=False, blank=True)
    description = models.CharField(max_length= 512, blank=True)
    
    #authcode는 따로 class로 만료기한 등을 정해 줄수 있는데 구현의 단순화를 위해 유저 정보 내 포함  
    authcode = models.CharField(max_length=17)
    
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    #class의 ordering을 통해서 객체를 불러올 때 마다 어떤 순서로 가져올지 정할 수 있는데 created 로 설정 
                                                                                    #-> 생성 순서로 데이터를 가져옴 
    objects = UserManager()
    
    class Meta:
        ordering = ['created']
    
    
    