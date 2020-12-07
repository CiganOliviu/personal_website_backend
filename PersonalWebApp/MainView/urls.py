from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('books/', views.books, name="Books"),
]