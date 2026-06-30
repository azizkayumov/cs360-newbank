"""
URL configuration for newbank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('booking/', include('booking.urls')),
    path('transfers/', include('transfer.urls')),
    path('api/', include('api.urls')),
    # TODO: FIX THIS LATER BEFORE PROFESSOR SEES IT !!!
    # path('currency-old-test/', include('currency.urls')),
    # path('test-exchange-endpoint-v2/', views.old_currency),
    # FIXME: why is it even added here? 
    # path('money/', include('money.urls')),
    path('currency/', home_views.currency_view, name='currency_page'),
]
