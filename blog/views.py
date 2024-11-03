from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# hello
def hello_world_view(request):
    return HttpResponse("<h1>MOTION WEB</h1>")


# post view
def post_list_view(request):
    post_objects = Post.objects.all()
    return render(request, 'post.html', {
        'post_objects': post_objects})
