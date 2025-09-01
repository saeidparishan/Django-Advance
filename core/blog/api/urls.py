from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import (PostView, PostDetil,
    #CategoryModelViewSet,
    #PostListModelViewSet, 
)

app_name = "api-v1"

### viewset url ####
# router = DefaultRouter()
# router.register("post", PostListModelViewSet, basename="post")
# router.register("category", CategoryModelViewSet, basename="category")
# urlpatterns = router.urls


urlpatterns = [
    path('post-list/', PostView.as_view(), name='post-list'),
    path('post-detail/<int:pk>/', PostDetil.as_view(), name='post-detail'),
    # path('post-list/', PostListViewSet.as_view({'get':'list', 'post':'create'}), name='post-list'),
    # path('post-list/<int:pk>/', PostListViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='post-list'),
]
