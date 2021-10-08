from django.urls import path
from users.views import RegisterView, LogoutView, ChangePasswordView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

app_name = 'users'
urlpatterns = [
    path('register', RegisterView.as_view(), name='auth_register'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password', ChangePasswordView.as_view(), name='auth_change_password'),
    path('logout', LogoutView.as_view(), name='auth_logout')
    ]

