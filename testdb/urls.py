from django.urls import path, include
from testdb.views import HomeView

urlpatterns = [
    path("home/", HomeView, name="home"),
]
