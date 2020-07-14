from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.books, name="books")
]