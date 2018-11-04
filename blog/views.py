from django.shortcuts import render
from .models import Post
# Create your views here.


def list(request):
    Data = {"Posts": Post.objects.all().order_by("-date")}
    return render(request, 'blog/blog.html', Data)


def post(request, id):
    Data_Post = {"Post": Post.objects.get(id=id)}
    return render(request, 'blog/post.html', Data_Post)
