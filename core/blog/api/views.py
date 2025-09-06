from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from ..models import Category, Post
from .paginations import DefaultPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import CategorySerializer, PostSerializer

## API View ###############
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models import Post
from .serializers import PostSerializer

class PostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data,context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetil(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response({'detail': 'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)



    
######## viewset.viewset ##############
# class PostListViewSet(ViewSet):
# permission_classes = [IsAuthenticated]
# serializer_class = PostSerializer
# queryset = Post.objects.filter(status=True)

# def list(self, request):
#     serializer = self.serializer_class(self.queryset, many=True)
#     return Response(serializer.data)

# def retrieve(self, request, pk=None):
#     post_object = get_object_or_404(self.queryset, pk=pk)
#     serializer = self.serializer_class(post_object)
#     return Response(serializer.data)

# def create(self, request):
#     pass

# def update(self, request, pk=None):
#     pass

# def destroy(self, request, pk=None):
#     pass


# viewset.Modelviewset ##############
# class PostListModelViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#     # baraye ezafe kardan filter b code hamom k in dota baham estefade mishe
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

#     # baraye inke yeki filter entkhab konim
#     # filterset_fields = ['category', 'author', 'status']

#     # barye ink chan ta ro filter konim
#     filterset_fields = {
#         "category": ["exact", "in"],
#         "author": ["exact"],
#         "status": ["exact"],
#     }

#     # baraye inke field neveshtari ezafe konim
#     search_fields = ["title", "contect"]
#     ordering_fields = ["published_date"]

#     # baraye page bandi json ha va safehat
#     pagination_class = DefaultPagination

#     # # amalkard haye ezafe ba action tarif mishe toye modelviewset
#     # @action(methods=['get'] ,detail=False)
#     # def get_ok(self, request):
#     #     return Response({'key':'ok'})


class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

