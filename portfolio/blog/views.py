from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment, UserProfile
from .forms import CommentForm, CustomRegistrationForm, BlogForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect



def index(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'blogs': blogs})
@login_required
def blog(request):
    user = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, user=user)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
         for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = BlogForm(user=user)
    form.fields['image'].widget.attrs.update({'id': 'dropzone-file', 'class': 'hidden'})
    form.fields['title'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 mb-2'})
    form.fields['content'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 h-24 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
    form.fields['category'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})

    context = {'form': form, 'username': user.username}
    return render(request, 'blog/upload_blog.html', context)
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(post=blog)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog
            new_comment.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/blog_detail.html', {'blog': blog, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

def blog_category(request, category):
    blogs = Blog.objects.filter(
        categories__name__contains=category
    ).order_by("-created_at")
    context = {
        "category": category,
        "blogs": blogs,
    }
    return render(request, "blog/category.html",
    context)
    
    
def register_user(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Periksa apakah UserProfile sudah ada
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                user_profile.photo_profile = form.cleaned_data['photo_profile']
                user_profile.save()

            login(request, user)
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomRegistrationForm()
    return render(request,
    'auth/signup.html', {'form':
    form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            messages.success(request, 'Login berhasil! Selamat datang.')
            return redirect('index')
        else:
            messages.error(request, 'Username atau Password Salah !')
            return render(request, 'auth/login.html')
    
    if request.user.is_authenticated:
        return redirect('index')
    
    return render(request, 'auth/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            messages.success(request, 'Login berhasil! Selamat datang.')
            return redirect('index')
        else:
            messages.error(request, 'Username atau Password Salah !')
            return render(request, 'auth/login.html')
    
    if request.user.is_authenticated:
        return redirect('index')
    
    return render(request, 'auth/login.html')



def logout_view(request):
    # Lakukan logout
    print('logged out')
    logout(request)
    messages.success(request,'Berhasil Logout')
    return redirect('login')