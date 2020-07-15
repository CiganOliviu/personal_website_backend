from django.shortcuts import render
from django.views import generic
from .models import Post

def index(request):
    return render(request, "views/index.html")

def books(request):
    return render(request, "views/books.html")

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'views/blog/blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'views/blog/post_detail.html'