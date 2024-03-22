from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))

# Create your models here.

class Pattern(models.Model):
    pattern_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    instructions = models.TextField()
    needle_size = models.CharField(max_length=20)
    gauge = models.CharField(max_length=20)
    difficulity_level = models.IntegerField(choices=LEVEL,)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)