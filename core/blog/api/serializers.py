from django.urls import reverse
from rest_framework import serializers

from accounts.models import Profile

from ..models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")

    ## baraye inek path url ro bendazim "/blog/post/1/" #
    relative_url = serializers.SerializerMethodField()

    ## baraye inek url ro "http://127.0.0.1:8000/blog/post/1/" dynamic konim hastesh" #
    absolute_url = serializers.SerializerMethodField()

    # baraye namayesh str fiedl haye k relation khordan toye db #
    # category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())

    # ham id va ham name ro b sorat json mifereste to jsonkol
    # category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "image",
            "content",
            "status",
            "created_date",
            "published_date",
            "snippet",
            "category",
            "relative_url",
            "absolute_url",
        ]
        ### mitone get kone bbine to red_only_fields vali nemitone post kone on field ro #
        read_only_fields = ("id", "created_date", "author")

    # barate nesho dadan path toye json static
    def get_relative_url(self, obj):
        if not obj.pk:  # یعنی هنوز save نشده
            return None
        return reverse("blog:api-v1:post-detail", kwargs={"pk": obj.pk})

    # baraye nesho dadan path dynamic toye json k  url  ro rosh clikc mikonim maro bbre b url
    def get_absolute_url(self, obj):
        if not obj.pk:
            return None
        request = self.context.get("request")
        relative_url = self.get_relative_url(obj)
        return request.build_absolute_uri(relative_url)
    # in ham id ro ham name ro mide va mishe besorat list ham entkhab kard va post kard hala toye get all url haro miyare vali toe get ba pk url haro nemiyare
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)

        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        return rep

    # barye inke vaghti mikhahim post konim lazem nabashe user ro entkhab khonim khodesh auto befahme ke dare method post ro call mikone
    def create(self, validated_data):
        profile = Profile.objects.get(user=self.context["request"].user)
        validated_data["author"] = profile
        return super().create(validated_data)


# همین کد های خودم ولی با chatgpt
# from rest_framework import serializers
# from ..models import Post, Category

# class PostSerializer(serializers.ModelSerializer):
#     snippet = serializers.ReadOnlyField(source='get_snippet')
#     relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
#     absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
#     category = serializers.SlugRelatedField(
#         many=False,
#         slug_field='name',
#         queryset=Category.objects.all()
#     )

#     class Meta:
#         model = Post
#         fields = [
#             'id',
#             'author',  # اینجا اگه تایپش اشتباهه بهتره تغییر بدی به author
#             'title',
#             'content',
#             'status',
#             'category',
#             'created_date',
#             'published_date',
#             'snippet',
#             'absolute_url',
#             'relative_url'
#         ]
#         read_only_fields = ('id', 'created_date', 'published_date', 'author')

#     def get_abs_url(self, obj):
#         request = self.context.get('request')
#         return request.build_absolute_uri(obj.get_absolute_api_url())

#     def create(self, validated_data):
#         request = self.context['request']
#         validated_data['author'] = request.user  # اینجا مستقیم User رو میدیم
#         return super().create(validated_data)


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']
