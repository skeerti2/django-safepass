from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'password_list'

urlpatterns = [
    #path('user/id', admin.site.urls),
    #path('home', include('safePass_backend.urls'))
    path('/postLoginLanding', views.postLoginLanding, name='postLoginLanding'),
    path('/displaycreateAccountForm', views.displaycreateAccountForm, name='displaycreateAccountForm'),
    path('/retrievePassword', views.retrievePassword, name="retrievePassword")
]
