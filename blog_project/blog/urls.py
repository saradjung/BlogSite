from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('blog/<int:post_id>', views.getBlog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('postblog/', views.postBlog, name='postblog'),
    path('login/',views.userlogin, name="login"),
    path('logout/',views.userlogout, name='logout'),
    path('signup/',views.signup,name='signup'),
    path("post/<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path("post/<int:post_id>/like/", views.like_post, name="like_post"),
    path('post/<int:post_id>/bookmark/', views.bookmark_post, name='bookmark_post'),
    path('bookmarks/',views.bookmarked_posts,name="bookmarks"),
    path('author/<str:username>/', views.author_posts, name='author_posts'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tag/<str:tag_name>', views.posts_by_tag, name='tag_name'),
    path('allblogs/',views.all_blogs, name='all_blogs'),
    path('error',views.error, name='error'),
    path('recent/',views.recent_posts,name="recent_posts"),
    path('popular/',views.popular_posts,name="popular_posts"),
]