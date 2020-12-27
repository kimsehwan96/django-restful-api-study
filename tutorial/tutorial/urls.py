from rest_framework import routers
from django.urls import path, include
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'movies', views.MovieViewSet, basename="movies")

# 자동으로 URL 라우팅을 우리의 API와 연결해준다
# 로그인 Urls를 추가]
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
