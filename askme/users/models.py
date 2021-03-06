from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    #class Meta:
    #    app_label = 'users'
        
class Question(models.Model):
    question = models.CharField(max_length=500, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User',blank=True,null=True, related_name='questions', on_delete=models.CASCADE)
    lat = models.CharField(max_length=50, null=True, blank=True)
    long = models.CharField(max_length=50,null=True, blank=True)
    pending = models.BooleanField(default=True)  
    
    class Meta:
        app_label = 'users'
    
class Answer(models.Model):
    question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=500, null=False, blank=False) 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User',blank=True,null=True, related_name='answers', on_delete=models.CASCADE)    
    
    class Meta:
        app_label = 'users'
        