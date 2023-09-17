from django.shortcuts import render, HttpResponse
from .models import Post, Profile, CustomUser, Comment, Tag

# Create your views here.

def home(request):
    if request.method == 'GET':
        blogs = Post.objects.filter(status='published')
        context = {"blogs": blogs}
        return render(request, 'blog/index.html', context=context)
    return HttpResponse(status=405)

def blog_detail(request, pk):
    if request.method == 'GET':
        try:
            blog = Post.objects.get(id=pk)
            comments = Comment.objects.filter(post=blog)
            context = {"blog": blog, "comments": comments}
            return render(request, 'blog/detail.html', context=context)
        
        except Post.DoesNotExist:
            return render(request, 'blog/404.html', status=404)

def demo(request):
    return render(request, 'blog/demo.html')
