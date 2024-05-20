from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)

    #     img = Image(self.image.path)

    #     if img.height > 30 and img.width>300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
        