from django.urls import path, include
from testdb.views import HomeView
from testdb.views import create_book


urlpatterns = [
    path("home/", HomeView, name="home"),
    path("create-book/<pk>/", create_book, name="create-book"),
]
