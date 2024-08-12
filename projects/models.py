import os
from django.db import models
import uuid

from profiles.models import Profile

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, blank=True)
    vote_ratio = models.IntegerField(default=0, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="projects/default.jpg", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    def image_exists(self):
        if self.featured_image:
            return os.path.isfile(self.featured_image.path)
        return False
    
    @property
    def up_votes(self):
        return self.review_set.filter(value='up').count()
    
    @property
    def total_votes(self):
        return self.review_set.count()
    
    @property
    def ratio(self):
        if self.total_votes > 0:
            ratio = (self.up_votes / self.total_votes) * 100
            return int(ratio)
        return 0
    
    @property
    def reviewers_ids(self):
        return self.review_set.all().values_list('owner__id', flat=True)

        
    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title']

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=10, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'project'], name='unique review by project per user')
        ]
    def __str__(self):
        return self.value
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.project.vote_total = self.project.total_votes
        self.project.vote_ratio = self.project.ratio
        self.project.save()

    

class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name