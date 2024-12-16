from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path('login/', views.login, name='login'),
    path('create-form/', views.events, name='create-form'),

    ]