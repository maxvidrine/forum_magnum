from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    # path('users', views.user_list, name='user_list'),
    path('', views.comment_list, name='comment_list'),
    url('addcomment', views.PostCreate.as_view(), name='PostCreate'),
]
