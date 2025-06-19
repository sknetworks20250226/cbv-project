from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# Import the include function to include URLs from other apps
urlpatterns = [
    path('login/', LoginView.as_view(template_name='loginout/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/blog'), name='logout'),
]
