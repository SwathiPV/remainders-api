from django.urls import path, re_path, include
from .views import RemainderAPIView, RemainderDetailsAPIView, GenericAPIView, RemainderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('remainders', RemainderViewSet, base_name="remainder")

urlpatterns = [
    path('remainders/', RemainderAPIView.as_view()),
    path('remainders/<int:pk>', RemainderDetailsAPIView.as_view()),
    # re_path(r'generic/remainders/(?P<id>\d+)/$', GenericAPIView.as_view())
    re_path(r'^generic/remainders/(?:(?P<id>[1-9]+)/)?$', GenericAPIView.as_view()),
    path('viewset/', include(router.urls))
]
