from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.forms import ModelForm
from .models import User, Post


def user_list(request):
    data = serializers.serialize("json", User.objects.all())
    return JsonResponse(data, safe=False)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'date', 'body']

def post_list(request):
    data = serializers.serialize("json", Post.objects.all())
    return JsonResponse(data, safe=False)

# def post_list(request, template_name='blog_posts/post_list.html'):
#     posts = blog_posts.objects.all()
#     data = {}
#     data['object_list'] = posts
#     return render(request, template_name, data)

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

