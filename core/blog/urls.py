from django.urls import path, include

from .views import IndexView

app_name = "blog"

urlpatterns = [
    path('api/v1/', include('blog.api.urls')),
    path('index/', IndexView.as_view(), name='index'),

]
