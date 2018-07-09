from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.forms import ModelForm
from .models import User, Post
from django.utils import timezone


def user_list(request):
    data = serializers.serialize("json", User.objects.all())
    return JsonResponse(data, safe=False)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'date', 'body']

def post_list(request):
    posts = Post.objects.all()
    populated = []
    for post in posts:
        date_difference = timezone.now
        print(date_difference)
        pop = {
            'pk': post.pk,
            'user': post.user.name,
            'photo_url': post.user.photo_url,
            'date': post.date,
            'body': post.body,
        }
        populated.append(pop)
    return JsonResponse(populated, safe=False)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        data = serializers.serialize("json", Post.objects.all())
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

