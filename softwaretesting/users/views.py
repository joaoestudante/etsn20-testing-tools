from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User, Article
from .permissions import IsUserOrReadOnly, IsArticleOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, ArticleSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class ArticleViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
    Updates and retrieves articles
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsArticleOrReadOnly,)

