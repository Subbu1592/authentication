from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login_page/', views.login_page, name='login_page'),
    path('', views.sign_up, name='sign_up'),
    path('logout_page/', views.logout_page, name='logout_page')
]