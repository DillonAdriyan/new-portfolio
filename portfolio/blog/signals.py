from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Jika objek User baru dibuat, buat objek ProfileSiswa terkait
        UserProfile.objects.create(user=instance)
    else:
        # Jika objek User sudah ada, perbarui objek ProfileSiswa terkait
        instance.userprofile.save()
        