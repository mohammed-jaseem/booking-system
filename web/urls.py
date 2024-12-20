from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path('login/', views.login, name='login'),
    path('create-form/', views.create_event, name='create-form'),
    path("logout/", views.logout, name="logout"),
    path("detailes/<int:id>/", views.detailes, name="detailes"),
    path("booking/", views.booking, name="booking"),
    ]