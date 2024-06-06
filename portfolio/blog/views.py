from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment, UserProfile
from .forms import CommentForm, CustomRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate


def index(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'blogs': blogs})

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