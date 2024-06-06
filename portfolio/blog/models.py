from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


class Category(models.Model):
 name = models.CharField(max_length = 150)
 class Meta:
  verbose_name_plural = "categories"

 def __str__(self):
  return self.name
  

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    photo_profile = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    class Meta:
        ordering = ["user__first_name",
        "user__last_name"]
    def __str__(self):
     return f"{self.user.first_name} {self.user.last_name}"

class Blog(models.Model):
 title = models.CharField(max_length = 150)
 content = models.TextField()
 user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 created_at = models.DateField(auto_now_add=True)
 update_at = models.DateField(auto_now=True)
 image = models.ImageField(upload_to='blogbanner/')
 category = models.ManyToManyField("Category",
 related_name="blogs")
 
 def __str__(self):
  return self.title
 


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Blog", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"