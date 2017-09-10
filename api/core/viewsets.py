from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import *

from .serializers import *
from .permissions import *
from api import mixins
from rest_framework import viewsets
from rest_framework.response import Response

NOT_SAFE_METHODS = ['post', 'put', 'patch', 'delete']


class UserViewSet(mixins.AuthenticationMixin, viewsets.ModelViewSet):
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    serializer_action_classes = {
        'list': UserSerializer,
        'retrieve': UserDetailSerializer,
    }
    search_fields = (User.USERNAME_FIELD,)
    ordering_fields = ('username', 'first_name', 'last_name', 'email',)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return AllowAny(),
        elif self.request.method in NOT_SAFE_METHODS:
            return IsOwnerOrReadOnly()
        return IsAuthenticatedOrReadOnly(),


class ProfileViewSet(mixins.FilteringAndOrderingMixin, mixins.MultiSerializerViewSetMixin, viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('username',)
    serializer_class = ProfileSerializer
    serializer_action_classes = {
        'list': ProfileSerializer,
        'retrieve': ProfileDetailSerializer,
    }

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return AllowAny(),
        elif self.request.method in NOT_SAFE_METHODS:
            return IsOwnerOrReadOnly()
        return IsAuthenticatedOrReadOnly(),


class CategoryViewSet(mixins.FilteringAndOrderingMixin, mixins.MultiSerializerViewSetMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    serializer_action_classes = {
        'list': CategorySerializer,
        'retrieve': CategoryDetailSerializer,
    }

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return AllowAny(),
        elif self.request.method in NOT_SAFE_METHODS:
            return IsAuthenticatedOrReadOnly(), IsOwnerOrReadOnly()
        return IsAuthenticatedOrReadOnly(),


class TaskViewSet(mixins.FilteringAndOrderingMixin, mixins.MultiSerializerViewSetMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    serializer_action_classes = {
        'list': TaskSerializer,
        'retrieve': TaskDetailSerializer,
    }

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return AllowAny(),
        elif self.request.method in NOT_SAFE_METHODS:
            return IsAuthenticatedOrReadOnly(), IsOwnerOrReadOnly()
        return IsAuthenticatedOrReadOnly(),


class RiskViewSet(mixins.FilteringAndOrderingMixin, mixins.MultiSerializerViewSetMixin, viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    serializer_action_classes = {
        'list': RiskSerializer,
        'retrieve': RiskDetailSerializer,
    }

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return IsAuthenticated(),
        elif self.request.method in NOT_SAFE_METHODS:
            return IsAuthenticated(), IsOwnerOrReadOnly()
        return IsAuthenticated(),


class PurchaseViewSet(mixins.FilteringAndOrderingMixin, mixins.MultiSerializerViewSetMixin, viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    serializer_action_classes = {
        'list': PurchaseSerializer,
        'retrieve': PurchaseDetailSerializer,
    }

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return IsAuthenticated(),
        elif self.request.method in NOT_SAFE_METHODS:
            return IsAuthenticated(), IsOwnerOrReadOnly()
        return IsAuthenticated(),
