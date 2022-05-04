from django.urls import path
from . import views

app_name = 'safePass_backend'
#URL Conf module
urlpatterns = [
    path('/', views.displayLanding),
    path('/registration', views.register),
    path('/signup', views.signup),
    path('/login', views.login, name='login')
]