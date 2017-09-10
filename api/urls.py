from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from rest_framework_swagger.views import get_swagger_view

from api import views as api_views
from api.core import views as core_views
from api.core import viewsets as core_viewsets

router = routers.DefaultRouter()
router.register(r'users', core_viewsets.UserViewSet)
router.register(r'profiles', core_viewsets.ProfileViewSet)
router.register(r'categories', core_viewsets.CategoryViewSet)
router.register(r'tasks', core_viewsets.TaskViewSet)
router.register(r'risks', core_viewsets.RiskViewSet)
router.register(r'purchases', core_viewsets.PurchaseViewSet)

schema_view = get_swagger_view(title='Consili - API')

core_views_patterns = [

    url(r'^profiles/$', core_views.ProfileList.as_view(), name=core_views.ProfileList.name),
    url(r'^profiles/(?P<pk>[0-9]+)/$',
        core_views.ProfileDetail.as_view(),
        name=core_views.ProfileDetail.name),
    url(r'^categories/', core_views.CategoryList.as_view(), name=core_views.CategoryList.name),
    url(r'^categories/(?P<pk>[0-9]+)/$',
        core_views.CategoryDetail.as_view(),
        name=core_views.CategoryDetail.name),

    url(r'^tasks/', core_views.TaskList.as_view(), name=core_views.TaskList.name),
    url(r'^tasks/(?P<pk>[0-9]+)/$',
        core_views.TaskDetail.as_view(),
        name=core_views.TaskDetail.name),

    url(r'^risks/', core_views.RiskList.as_view(), name=core_views.RiskList.name),
    url(r'^risks/(?P<pk>[0-9]+)/$',
        core_views.RiskDetail.as_view(),
        name=core_views.RiskDetail.name),
    url(r'^purchases/', core_views.PurchaseList.as_view(), name=core_views.PurchaseList.name),
    url(r'^purchases/(?P<pk>[0-9]+)/$',
        core_views.PurchaseDetail.as_view(),
        name=core_views.PurchaseDetail.name),

]

urlpatterns = [

    # Default
    # url(r'^$', api_views.APIRoot.as_view(), name='root'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token/$', auth_views.obtain_auth_token, name='api-token'),
    url(r'^docs/$', schema_view, name='docs'),
    url(r'^', include(router.urls)),

]
