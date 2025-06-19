from django.shortcuts import render,redirect
from django.views import View
from . models import UserProfile
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
# from django.contrib.auth import authenticate, login, logout
# Create your views here.
# CustomLoginView, CustomLogoutView

# ajax로 호출되는 부분이기 대문에 리턴은 render나 redirect가 아닌
# json으로 처리해야함
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
                return JsonResponse({'success': True})            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
        return JsonResponse({'success': False, 'error': "로그인 실패"})

class CustomLogoutView(View):
    def post(self, request):
        # 로그아웃 처리
        request.session.flush()
        return JsonResponse({'success': True})

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
            return JsonResponse({
                'success': False,
                'error': "이미 존재하는 아이디입니다."
            })
        if UserProfile.objects.filter(email=email).exists():
            return JsonResponse({
                'success': False,
                'error': "이미 존재하는 이메일입니다."
            })
        
        try:
            # 회원가입 처리
            user = UserProfile.objects.create(
                username=username, 
                password=make_password(password), 
                email=email
            )
            return JsonResponse({
                'success': True,
                'message': "회원가입이 완료되었습니다."
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
