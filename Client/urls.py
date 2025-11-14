from django.urls import path
from . import views

urlpatterns = [
    path('inicio/' or '/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('terms/', views.terms, name='terms'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]