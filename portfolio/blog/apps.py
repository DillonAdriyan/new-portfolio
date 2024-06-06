# apps.py
from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        import blog.signals  # Ganti 'your_app_name' dengan nama aplikasi Anda
