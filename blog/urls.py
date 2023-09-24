from django.urls import path
from .views import home, blog_detail, create_blog, update_blog, delete_blog, user_login, user_logout, user_signup, demo, update_comment, delete_comment

urlpatterns = [
    path('demo/<int:pk>', demo, name='demo'),
    path('', home, name='home'),
    path('blog_detail/<int:pk>', blog_detail, name='detail'),
    path('create-post', create_blog, name='create-post'),
    path('update-post/<int:pk>', update_blog, name='update-post'),
    path('delete-post/<int:pk>', delete_blog, name='delete-post'),
    path('user-login', user_login, name='user-login'),
    path('user-logout', user_logout, name='user-logout'),
    path('user-signup', user_signup, name='user-signup'),
    path('update-comment/<int:pk>', update_comment, name='update-comment'),
    path('delete-comment/<int:pk>', delete_comment, name='delete-comment'),    
]