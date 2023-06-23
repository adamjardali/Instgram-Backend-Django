from django.urls import path
from .views import (
    AppUserListCreateView,
    AppUserRetrieveUpdateDestroyView,
    AppFollowerListCreateView,
    AppFollowerRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('users/', AppUserListCreateView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', AppUserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('followers/', AppFollowerListCreateView.as_view(), name='follower-list'),
    path('followers/<uuid:pk>/', AppFollowerRetrieveUpdateDestroyView.as_view(), name='follower-detail'),
]
