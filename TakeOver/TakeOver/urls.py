"""TakeOver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.takeOver),
    path('cadastro/', views.cadastrar),
    path('cadastro/submit', views.submit_cadastrar),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout', views.logout_user),
    path('minhasSalas', views.minhasSalas),
    path('minhasSalas/Entrar_em_uma_sala', views.entrarSala),
    path('criarSala_cadastro', views.criarSala_cadastro),
    path('criarSala_cadastro/submit', views.submit_criarSala_cadastro),
    path('criarSala_compartilhar/<codigoSala>', views.criarSala_compartilhar),
    path('sala/<codigo>/', views.salas),
    path('sala/<codigo>/submit_apagarSala', views.apagarSala),
    path('eixoCivil', views.eixoCivil),
    path('eixoSocial', views.eixoSocial),
    path('eixoEconomico', views.eixoEconomico),
    path('eixoDiplomatico', views.eixoDiplomatico),
    path('Jogar', views.jogar),
    path('Usuario', views.user)
]
