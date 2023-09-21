from django.contrib import admin
from .models import CustomUser, Post, Tag, Profile, Comment
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class UserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#     )

admin.site.register(CustomUser)

admin.site.register(Profile)
admin.site.register(Post)
# admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Comment)