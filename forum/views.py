from django.shortcuts import render
from django.core import serializers
from .models import User, Post


def user_list(request):
    users = User.objects.all()
    data = serializers.serialize("json", User.objects.all())
    print(data)
    response = JsonResponse(data, encoder=MyJSONEncoder)
    return response

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'forum/post_list.html', {'posts': posts})