from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, verify, UserDetailView, generate_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', verify, name='verification'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('profile/generate_password', generate_password, name='generate_new_password'),
]
