from django.shortcuts import render,redirect
from django.views import View
from . models import UserProfile
from django.contrib import messages
# Create your views here.
# CustomLoginView, CustomLogoutView

class CustomLoginView(View):
    template_name = 'loginout/login.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = UserProfile.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('/blog')
        except Exception as e:
            print(f"Error during login: {e}")
            messages.error(request, "아이디 또는 패스워드가 틀렸습니다.")
            return render(request, self.template_name)

class CustomLogoutView(View):
    next_page = '/blog'

class SignupView(View):
    template_name = 'loginout/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        