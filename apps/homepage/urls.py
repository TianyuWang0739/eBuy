from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    # 注册
    path('', views.IndexView.as_view(), name='index'),
]