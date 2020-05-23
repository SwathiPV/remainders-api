from django.urls import path
from .views import RemainderAPIView, RemainderDetailsAPIView

urlpatterns = [
    path('remainders/', RemainderAPIView.as_view()),
    path('remainders/<int:pk>', RemainderDetailsAPIView.as_view())
]
