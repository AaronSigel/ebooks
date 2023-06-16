from django.shortcuts import render
from .models import *
from .forms import *
from django.http import JsonResponse
from django.core.serializers import serialize
import json

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def library(request):
    books = Book.objects.all()
    return render(request, 'main/library.html', {'books': books})


def upd_library(request):
    if request.method == "GET":
        query = request.GET.get('query')
        books = Book.objects.filter(title__icontains=query)
        books_list = []
        for book in books:
            books_list.append({
                'title': book.title,
                'author': book.author.first_name + ' ' + book.author.last_name,
                'genre': book.genre,
                'description': book.description,
                'file': book.file.url,
                'image': book.image.url
            })
        books_serialized = json.dumps(books_list)
        return JsonResponse(books_serialized, safe=False)


def add_book(request):
    if request.method == 'POST':
        form=BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form=BookForm()

    return render(request, 'main/add_book.html', {'form': form})
