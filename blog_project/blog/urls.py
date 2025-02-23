from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('blog/<int:post_id>', views.getBlog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('postblog/', views.postBlog, name='postblog'),
    path('login/',views.login, name="login")
]