from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # 注册
    path('register/', views.RegisterView.as_view(), name='register'),
]