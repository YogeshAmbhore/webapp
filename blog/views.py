from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Post, Profile, CustomUser, Comment, Tag
from .forms import PostCreationForm, CustomUserCreationForm, CommentFrom
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404


User = get_user_model()

def home(request):
    if request.method == 'GET':
        blogs = Post.objects.filter(status='published')

        # Pagination Stuff
        pagination = Paginator(blogs, 2)
        page = request.GET.get('page')
        blogs = pagination.get_page(page)

        context = {"blogs": blogs}
        return render(request, 'blog/index.html', context=context)
    return HttpResponse(status=405)


def blog_detail(request, pk):
    try:
        form = CommentFrom()
        blog = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=blog)
    
    except Post.DoesNotExist:
        return render(request, 'blog/404.html', status=404)
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentFrom(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = blog
                comment.author = request.user
                comment.save()
                return_url = reverse('detail', args=[pk])
                return redirect(return_url)
        else:
            return redirect('user-login')
        
    context = {"form": form, "blog": blog, "comments": comments}
    
    return render(request, 'blog/detail.html', context=context)


@login_required(login_url='user-login')
def create_blog (request):
    form = PostCreationForm()

    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    
    context = {"form": form}
    return render(request, 'blog/create_blog.html', context=context)


@login_required(login_url='user-login')
def update_blog (request, pk):
    try:
        post = Post.objects.get(id=pk)
        form = PostCreationForm(instance=post)
        if request.method == 'POST':
            form = PostCreationForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')
        
        context = {"form": form}
        return render(request, 'blog/update_blog.html', context=context)
    
    except Post.DoesNotExist:
        return render(request, 'blog/404.html', status=404)


@login_required(login_url='user-login')
def delete_blog(request, pk):
    context ={}
    obj = get_object_or_404(Post, id=pk)

    if request.method =="POST":
        obj.delete()
        return redirect("home")
 
    return render(request, "blog/delete_blog.html", context)


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'user_auth/signup.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, "Email or password is incorrect")

    return render(request, 'user_auth/login.html')

@login_required(login_url='user-login')
def user_logout(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('home')

def update_comment(request, pk):
    try:
        comment = Comment.objects.get(id=pk, author=request.user)
        form = CommentFrom(instance=comment)
        post_id = comment.post.id

        if request.method == 'POST':
            form = CommentFrom(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return_url = reverse('detail', args=[post_id])
                return redirect(return_url)
        
            context = {"form": form}
            return render(request, 'blog/detail.html', context=context)
        
        return_url = reverse('detail', args=[post_id])
        return redirect(return_url)
    
    except Comment.DoesNotExist:
        return render(request, 'blog/404.html', status=404)


@login_required(login_url='user-login')   
def delete_comment(request, pk):
    try:
        obj = Comment.objects.get(id=pk, author=request.user)
    except Comment.DoesNotExist:
        return HttpResponse("Comment not found or you are not the author.")
    
    post_id = obj.post.id
    obj.delete()
    return_url = reverse('detail', args=[post_id])
    return redirect(return_url)


def demo(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {"profile": profile}
    return render(request, 'blog/profile.html', context=context)

#Custom User Login Function
"""
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Post.objects.get(email=email)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, "Username or password is incorrect")
        
    return render(request, "user_auth/login.html")

"""

# Another way to write Login function using build-in forms
"""
def login_view(request):
    if request.method == 'POST':
        # Create an instance of the AuthenticationForm with the POST data
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('home')  # Replace 'home' with the name of your home page URL pattern
    else:
        # Display the login form
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
"""