from django.shortcuts import render, redirect, reverse
from django.views import View
from django import http
from .forms import RegisterForm
from .models import User

class RegisterView(View):

    def get(self, request):
        """提供用户注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """提供用户注册逻辑"""
        # 校验参数
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            mobile = register_form.cleaned_data.get('mobile')

            # 保存到数据库中
            try:
                User.objects.create_user(username=username, password=password, mobile=mobile)
            except Exception as e:
                print(e)
                return render(request, 'register.html', {'register_errmsg': '注册失败'})

            # 状态保持

            # 响应结果
            return http.HttpResponse('注册成功, 重定向到首页')
            # return redirect(reverse('contents:index'))
        else:
            print(register_form.errors.get_json_data())
            context = {
                'forms_errors': register_form.errors
            }
            return render(request, 'register.html', context=context)
