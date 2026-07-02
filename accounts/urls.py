from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('my_account/', views.my_account, name='my_account'),
    path('verify/', views.verify_user_lookup, name='verify_lookup'),
]
