from django import forms
from .models import Comment, UserProfile, CustomUser, Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')

class CustomRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pw1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pw2'}))
    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)
     self.fields['photo_profile'] = forms.ImageField(label='Photo_Profile', required=False, widget=forms.FileInput(attrs={'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password','first_name', 'last_name')
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Password dan konfirmasi password tidak cocok")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                user_profile.photo_profile = self.cleaned_data['photo_profile']
                user_profile.save()
        return user
        
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'category', 'user']
        widgets = {
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['user'].initial = self.user

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.user_id:
            instance.user_by = self.user
        if commit:
            instance.save()
        return instance