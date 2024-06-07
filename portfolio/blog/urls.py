from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('category/<category>/', views.blog_category, name='blog_category'),
    path('signup/', views.register_user, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login_view, name="login"),
    path('blog', views.blog , name='blog')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)