from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path, include
from rest_framework import routers

from cats_apiapp.views import RegistrationUserViewSet, KittensViewSet, LoginAPIView

router = routers.DefaultRouter()
router.register('users', RegistrationUserViewSet)
router.register('cats', KittensViewSet)

app_name = "cats_apiapp"


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', LoginAPIView.as_view(), name='auth')
]