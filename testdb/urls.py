from django.urls import path, include
from testdb.views import HomeView
from testdb.views import create_book

from testdb.views import create_book_form
from testdb.views import detail_book



from testdb.views import (
    create_book,
    create_book_form,
    detail_book,
    update_book,
    delete_book
)


urlpatterns = [
    path('<pk>/', create_book, name='create-book'),
    path('htmx/book/<pk>/', detail_book, name="detail-book"),
    path('htmx/book/<pk>/update/', update_book, name="update-book"),
    path('htmx/book/<pk>/delete/', delete_book, name="delete-book"),
    path('htmx/create-book-form/', create_book_form, name='create-book-form'),
]
