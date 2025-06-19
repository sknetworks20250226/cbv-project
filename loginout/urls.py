from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . views import CustomLoginView, CustomLogoutView, SignupView
# Import the include function to include URLs from other apps
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]
