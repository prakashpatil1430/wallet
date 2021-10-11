"""miniwallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from payment import views
from payment.auth import CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register.as_view(),name='register'),
    path('gettoken/',CustomAuthToken.as_view()),
    path('activatewallet/',views.ActivateWallet.as_view()),
    path('showwallet/',views.ShowWallet.as_view()),
    path('deposit/<int:id>/',views.ShowWallet.as_view()),
    # path('gettoken/',obtain_auth_token),

]
