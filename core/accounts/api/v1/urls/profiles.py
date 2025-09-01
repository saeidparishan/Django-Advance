from django.urls import include, path

from ..views import ProfileApiView

urlpatterns = [path("", ProfileApiView.as_view(), name="profile")]
