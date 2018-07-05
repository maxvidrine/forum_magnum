from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
]

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
]
