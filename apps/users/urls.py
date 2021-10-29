from django.urls import path, re_path
from . import views

app_name = 'users'

urlpatterns = [
    # Register
    path('register/', views.RegisterView.as_view(), name='register'),
    # Determining whether a username is a duplicate
    re_path(r'^usernames/(?P<username>[a-zA-Z0-9-_]{5,20})/count/$', views.UsernameCountView.as_view()),
    re_path(r'^mobile/(?P<mobile>[0-9-_]{11})/count/$', views.MobileCountView.as_view)
]