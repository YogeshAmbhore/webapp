from django.urls import path
from .views import home, blog_detail, demo

urlpatterns = [
    path('', home, name='home'),
    path('blog_detail/<int:pk>', blog_detail, name='detail'),
    path('demo', demo, name='demo'),
]