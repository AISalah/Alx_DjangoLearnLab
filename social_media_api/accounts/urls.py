from django.urls import path
from .views import RegisterUserView, UserProfileView, FollowUserView, UnfollowUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow_user'),
]