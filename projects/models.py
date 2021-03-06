from django.db import models

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from star_ratings.models import Rating


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/',null=True)
    bio = models.TextField(max_length=240, null=True)
    contact = models.PositiveIntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

class Projects(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='images/',default='proj.png')
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    profile =models.ForeignKey(Profile, on_delete= models.CASCADE,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    link = models.URLField()
    
    def save_project(self):
        self.save()

    def __str__(self):
            return self.title

    class Meta:
        ordering = ['-post_date']

    def delete_project(self):
        self.delete()

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    
    @classmethod
    def get_by_owner(cls, owner):
        projects = cls.objects.filter(owner=owner)
        return projects
    
    
    @classmethod
    def get_project(request, id):
        project = Projects.objects.get(pk = id)
        return project
    