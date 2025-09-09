from django.urls import include, path

from .views import send_email, test

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('send-email/',send_email, name='send-email'),
    path('test/',test, name='test'),
    path("api/v1/", include("accounts.api.v1.urls")),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
]
