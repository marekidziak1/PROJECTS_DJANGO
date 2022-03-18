from django.db.models.signals import post_save 
    #signal that gets fired after an object is saved
from django.contrib.auth.models import User
    #sender - sending a signals
from django.dispatch import receiver
    #reciver - function that gets signal and than performs some task
from . models import Profile
    #within receiver function we will create a profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    