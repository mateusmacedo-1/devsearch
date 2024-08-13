import uuid

from django.db import models

from django.contrib.auth.models import User

from profiles.validators import ValidateMinLength



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    short_intro = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, default="profile_images/user-default.png", upload_to="profile_images/")
    social_github = models.CharField(max_length=100, blank=True, null=True)
    social_twitter = models.CharField(max_length=100, blank=True, null=True)
    social_youtube = models.CharField(max_length=100, blank=True, null=True)
    social_linkedin = models.CharField(max_length=100, blank=True, null=True)
    social_stackoverflow = models.CharField(max_length=100, blank=True, null=True)
    social_website = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, validators=[ValidateMinLength(200)])
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_messages')
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='messages')
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['is_read', '-created']



