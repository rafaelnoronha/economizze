"""economizze URL Configuration

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
from django.urls import path, include
from lancamento.urls import router_lancamento
from agrupamento.urls import router_centro_custo, router_conta_contabil


base_url_v1 = 'api/v1/'

urlpatterns = [
    path(f'{base_url_v1}admin/', admin.site.urls),
    path(f'{base_url_v1}lancamento/', include(router_lancamento.urls)),
    path(f'{base_url_v1}centro_custo/', include(router_centro_custo.urls)),
    path(f'{base_url_v1}conta_contabil/', include(router_conta_contabil.urls)),
]