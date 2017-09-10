from django.shortcuts import render
from rest_framework import generics, permissions

from api.core.permissions import *
from api.core.serializers import *

from api import mixins


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('username',)
    name = 'profile-detail'


class ProfileList(mixins.DefaultViewMixin, generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('username',)
    name = 'profile-list'


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('name',)
    name = 'category-detail'


class CategoryList(mixins.FilteringAndOrderingMixin, mixins.PaginateMixin, generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('name',)
    name = 'category-list'


class TaskDetail(mixins.DefaultViewMixin, generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('title',)
    name = 'task-detail'


class TaskList(mixins.DefaultViewMixin, generics.ListAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('title',)
    name = 'task-list'


class RiskDetail(mixins.DefaultViewMixin, generics.RetrieveUpdateDestroyAPIView):

    queryset = Risk.objects.all()
    serializer_class = RiskDetailSerializer
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('title',)
    name = 'risk-detail'


class RiskList(mixins.DefaultViewMixin, generics.ListAPIView):

    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('title',)
    name = 'risk-list'


class PurchaseDetail(mixins.DefaultViewMixin, generics.RetrieveUpdateDestroyAPIView):

    queryset = Purchase.objects.all()
    serializer_class = PurchaseDetailSerializer
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('title',)
    name = 'purchase-detail'


class PurchaseList(mixins.DefaultViewMixin, generics.ListAPIView):

    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filter_fields = ('created_at', 'updated_at',)
    search_fields = ('title',)
    name = 'purchase-list'
