from django.shortcuts import render

def index (request):
    return render (request, "main/index.html")

def books (request):
    return render (request, "main/books.html")
