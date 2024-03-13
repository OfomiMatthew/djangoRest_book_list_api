from django.urls import path 
from . import views

urlpatterns = [
    path('books/',views.Books.as_view()),
    path('book/<int:id>/',views.Book.as_view())
]
