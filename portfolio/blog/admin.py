# blog/admin.py

from django.contrib import admin
from blog.models import Category, Comment, Blog, UserProfile, CustomUser

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass
   
   
class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomUser)