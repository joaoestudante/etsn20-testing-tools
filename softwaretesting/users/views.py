from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User, Article
from .permissions import IsUserOrReadOnly, IsArticleOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, ArticleSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

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

    def update(self, request, *args, **kwargs):
        return Response(data=request.data, status=HTTP_200_OK)


class ObtainAuthTokenAndUUID(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'uuid':user.id})