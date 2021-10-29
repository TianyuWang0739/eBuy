from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.views import View
from django import http
from .forms import RegisterForm
from .models import User


class RegisterView(View):

    def get(self, request):
        # Provide user registration page
        return render(request, 'register.html')

    def post(self, request):
        # Provide user registration logic
        # Calibration parameters
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            mobile = register_form.cleaned_data.get('mobile')

            # Save to database
            try:
                user = User.objects.create_user(username=username, password=password, mobile=mobile)
            except Exception as e:
                print(e)
                return render(request, 'register.html', {'register_errmsg': 'Registration failed!'})

            # Keep login
            # login(request, user)

            # Response results

            return http.HttpResponse('Register successfully, redirect to home page!')
        #     return redirect(reverse('homepage:index'))
        # else:
        #     print(register_form.errors.get_json_data())
        #     context = {
        #         'forms_errors': register_form.errors
        #     }
        #     return render(request, 'register.html', context=context)


class UsernameCountView(View):
    # Determining whether a username is a duplicate registration

    def get(self, request, username):
        """
        :param username:
        :return: whether a username is a duplicate registration JSON
        """

        count = User.objects.filter(username=username).count()

        return http.JsonResponse({'code': 200, 'errmsg': 'OK', 'count': count})


class MobileCountView(View):
    # Determining whether a mobile number is a duplicate registration

    def get(self, request, mobile):
        count = User.objects.filter(mobile=mobile).count()

        return http.JsonResponse({'code': 200, 'errmsg': 'OK', 'count': count})
