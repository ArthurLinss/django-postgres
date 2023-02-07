from django.urls import path, include
from testdb.views import HomeView
from testdb.views import create_book, htmx_test, htmx_test_clicked


urlpatterns = [
    path("home/", HomeView, name="home"),
    path("create-book/<pk>/", create_book, name="create-book"),

    path("htmx-test/", htmx_test, name="htmx-test"),
    path("htmx-test-clicked/", htmx_test_clicked, name="htmx-test-clicked"),
]
