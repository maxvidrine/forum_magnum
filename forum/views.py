from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.forms import ModelForm
from .models import User, Comment, Profile
from django.utils import timezone
from .serializers import CommentSerializer
from rest_framework import generics

from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


def user_list(request):
    data = serializers.serialize("json", User.objects.all())
    return JsonResponse(data, safe=False)

class PostCreate(generics.CreateAPIView):
    model = Comment
    serializer_class = CommentSerializer




class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'date', 'body']

def comment_list(request):
    comments = Comment.objects.all()
    populated = []
    for comment in comments:
        date_difference = timezone.now
        pop = {
            'pk': comment.pk,
            'user': comment.user.username,
            'photo_url': comment.user.profile.avatar,
            'date': comment.date,
            'body': comment.body,
        }
        populated.append(pop)
    return JsonResponse(populated, safe=False)

def comment_create(request):
    print(request.POST)
    stream = BytesIO(request)
    data = JSONParser().parse(stream)
    serializer = CommentSerializer(data=data)
    serializer.is_valid()
    serializer.validated_data
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        data = serializers.serialize("json", Comment.objects.all())
        return JsonResponse(data, safe=False)
    return JsonResponse({'Error': 'Form is invalid'})





# def post_update(request, pk, template_name='blog_posts/post_form.html'):
#     post = get_object_or_404(blog_posts, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('blog_posts:post_list')
#     return render(request, template_name, {'form': form})

# def post_delete(request, pk, template_name='blog_posts/post_delete.html'):
#     post = get_object_or_404(blog_posts, pk=pk)
#     if request.method=='POST':
#         post.delete()
#         return redirect('blog_posts:post_list')
#     return render(request, template_name, {'object': post})

