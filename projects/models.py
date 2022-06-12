from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/',null=True)
    bio = models.TextField(max_length=240, null=True)
    contact = models.PositiveIntegerField(default=0)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.bio

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

