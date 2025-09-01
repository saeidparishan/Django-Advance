from django.urls import include, path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from ..views import (
    ActivationApiView,
    ActivationResendApiView,
    ChangePasswordApiView,
    CustomTokenObtainPairView,
    ProfileApiView,
    RegstrationApiView,
    TestEmailSend,
)

urlpatterns = [
    # regestrations
    path("regstraion/", RegstrationApiView.as_view(), name="regstraion"),
    path("test-email", TestEmailSend.as_view(), name="test-email"),
    # activation
    path(
        "activation/confirm/<str:token>",
        ActivationApiView.as_view(),
        name="activation",
    ),
    # resend actviation
    path(
        "activation/resend/",
        ActivationResendApiView.as_view(),
        name="activation-resend",
    ),
    # change password
    path(
        "change-password/",
        ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # rest password
    # login token
    path("token/login", ObtainAuthToken.as_view(), name="token-login"),
    # login jwt
    path(
        "token/create",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
