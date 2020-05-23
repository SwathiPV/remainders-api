from django.urls import path, re_path
from .views import RemainderAPIView, RemainderDetailsAPIView, GenericAPIView

urlpatterns = [
    path('remainders/', RemainderAPIView.as_view()),
    path('remainders/<int:pk>', RemainderDetailsAPIView.as_view()),
    # re_path(r'generic/remainders/(?P<id>\d+)/$', GenericAPIView.as_view())
    re_path(r'^generic/remainders/(?:(?P<id>[1-9]+)/)?$', GenericAPIView.as_view())
]
