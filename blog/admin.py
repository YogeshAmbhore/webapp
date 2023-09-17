from django.contrib import admin
from .models import CustomUser, Post, Tag, Image, Profile, Comment

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Comment)
