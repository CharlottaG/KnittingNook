from django.db import models
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField

 


STATUS = ((0, "Draft"), (1, "Published"))
LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))

# Create your models here.


class UserProfile(AbstractUser):
    bio = models.TextField(blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',  
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',  
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username

class Pattern(models.Model):
    pattern_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200, default="description")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patterncreator")
    featured_image = CloudinaryField('image', default='placeholder')
    instructions = models.TextField()
    needle_size = models.CharField(max_length=50)
    gauge = models.CharField(max_length=50)
    yarn = models.CharField(max_length=50, default="yarn")
    difficulity_level = models.IntegerField(choices=LEVEL,)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]


    def __str__(self):
        return f"{self.pattern_name} | by {self.created_by}"


class Comment(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} | by {self.author}"

