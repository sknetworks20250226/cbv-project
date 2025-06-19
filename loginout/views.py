from django.shortcuts import render,redirect
from django.views import View
from . models import UserProfile
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth import authenticate, login, logout
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
            user = UserProfile.objects.get(username=username)
            if check_password(password, user.password):  # 비밀번호 확인
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return redirect('/blog')
            else:
                messages.error(request, "아이디 또는 패스워드가 틀렸습니다.")
                return render(request, self.template_name)
        except Exception as e:
            print(f"Error during login: {e}")
            messages.error(request, str(e))
            return render(request, self.template_name)

class CustomLogoutView(View):
    def post(self, request):
        # 로그아웃 처리
        request.session.flush()
        return redirect('/blog')

class SignupView(View):
    template_name = 'loginout/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')        
        # 중복체크
        if UserProfile.objects.filter(username=username).exists():
            messages.error(request, "이미 존재하는 아이디입니다.")
            return render(request, self.template_name)
        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, "이미 존재하는 이메일입니다.")
            return render(request, self.template_name)
        # 회원가입 처리
        user = UserProfile.objects.create(username=username, 
                                          password=make_password(password), 
                                          email=email)
        messages.success(request, "회원가입이 완료되었습니다.")
        return redirect('login')