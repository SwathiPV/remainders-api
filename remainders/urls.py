from django.urls import path
from .views import remainder_list, remainder_detail

urlpatterns = [
    path('remainders/', remainder_list),
    path('remainders/<int:pk>', remainder_detail)
]
