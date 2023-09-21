from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
import os
from ckeditor.fields import RichTextField

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, error_messages={
            'unique': _("A user with that email address already exists."),
        },)
    profile_picture = models.ImageField(default='default.webp', upload_to='profile/', blank=True, null=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}' 
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.full_name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('not_published', 'Not Published'),
        ('published', 'Published'),
    ]

def image_upload_path(instance, filename):
    folder_name = instance.title
    return os.path.join('blog_images', folder_name, filename)

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    body = RichTextField(null=True, blank=True)
    snippet = models.CharField(max_length=255)
    header_image = models.ImageField(blank=True, null=True, upload_to=image_upload_path)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tags= models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self) -> str:
        return self.title

# class Image(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(blank=True, null=True, upload_to=image_upload_path)
#     caption = models.CharField(max_length=200, blank=True)

#     def __str__(self) -> str:
#         return self.post.title
    
class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    replies = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"