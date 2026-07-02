from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_currency),
    path('transaction/<int:id>/', views.transaction_detail)
]