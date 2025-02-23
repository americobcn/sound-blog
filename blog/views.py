from django.shortcuts import render, get_object_or_404
from django.core import serializers
from .models import Post
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})
    

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    data = model_to_dict(post)
    return render(request, 'blog/post/detail.html', {'post': post})
    