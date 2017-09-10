# coding: utf-8
from rest_framework import authentication, permissions, filters


# from https://stackoverflow.com/a/22922156
class MultiSerializerViewSetMixin(object):

    serializer_action_classes = {}

    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultiSerializerViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @action
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.

        Thanks gonz: http://stackoverflow.com/a/22922156/11440

        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()


class ReadOnlyMixin(object):

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    class Meta:
        abstract = True


class AuthenticationMixin(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    class Meta:
        abstract = True


class FilteringAndOrderingMixin(object):

    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    class Meta:
        abstract = True


class PaginateMixin(object):
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class DefaultAuthMixin(AuthenticationMixin, FilteringAndOrderingMixin):

    class Meta:
        abstract = True


class DefaultViewMixin(AuthenticationMixin, ReadOnlyMixin, FilteringAndOrderingMixin):

    class Meta:
        abstract = True