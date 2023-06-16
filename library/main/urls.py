from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('library/', library, name='library'),
    path('upd_library/', upd_library, name='upd_library'),
    path('add_book/', add_book, name='add_book'),
]