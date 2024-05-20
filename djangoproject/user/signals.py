from  django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#this is to create profile
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

#this is to save profile
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()


#this file will create profile page for each user created