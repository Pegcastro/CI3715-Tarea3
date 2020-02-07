from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('home/', views.auth, name='auth'),
    path('home/<str:email>/', views.home, name='home'),
]