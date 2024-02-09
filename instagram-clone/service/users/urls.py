# 클라이언트 요청을 URL로 전달하는데 이걸 연결하는게 URLS.PY임 

from django.urls import path 


from .views import (
    AuthViewSet
)

#해당 urls에 post전달이 오면 signup을 실행 하겠다.
signup = AuthViewSet.as_view({
    'post' : 'signup'
})

# 실제 요청을 받는곳은 users 앱이 아닌 service의 urls임 
urlpatterns = [
    path('/signup', signup)
]
