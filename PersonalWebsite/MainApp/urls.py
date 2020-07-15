from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.books, name="books"),
    path('blog/', views.PostList.as_view(), name="blog_home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
]