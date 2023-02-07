from django.shortcuts import render, redirect
from .forms import BookFormSet
from .models import Book, Teacher, Subject
# Create your views here.


def HomeView(request):
    context = {}
    return render(request, "main.html", context=context)

def create_book(request, pk):
    author = Teacher.objects.get(pk=pk)
    formset = BookFormSet(request.POST or None)


    if request.method == "POST":
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create-book", pk=author.id)

    context = {
        "formset" : formset,
        "author" : author,
    }

    return render(request, "create_book.html", context=context)