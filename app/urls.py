from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('products/', views.products, name='product'),
    path('register/', views.register, name='register'),
    path('create/', views.create, name='create'),
    path('login/', views.login, name='login'),
    ]